```python
@wraps(Conv2D)
def DarknetConv2D(*args, **kwargs):
    """Wrapper to set Darknet parameters for Convolution2D."""
    darknet_conv_kwargs = {'kernel_regularizer': l2(5e-4)}
    darknet_conv_kwargs['padding'] = 'valid' if kwargs.get('strides')==(2,2) else 'same'
    darknet_conv_kwargs.update(kwargs)
    return Conv2D(*args, **darknet_conv_kwargs)
 
def DarknetConv2D_BN_Leaky(*args, **kwargs):
    """Darknet Convolution2D followed by BatchNormalization and LeakyReLU."""
    no_bias_kwargs = {'use_bias': False}
    no_bias_kwargs.update(kwargs)
    return compose(
        DarknetConv2D(*args, **no_bias_kwargs),
        BatchNormalization(),
        LeakyReLU(alpha=0.1))
```
Res_unit 由连续的两个Conv2D_BN_Leaky，再加一个add构成。
```python
def resblock_body(x, num_filters, num_blocks):
    '''A series of resblocks starting with a downsampling Convolution2D'''
    # Darknet uses left and top padding instead of 'same' mode
    x = ZeroPadding2D(((1,0),(1,0)))(x)
    x = DarknetConv2D_BN_Leaky(num_filters, (3,3), strides=(2,2))(x)
    for i in range(num_blocks):
        y = compose(
                DarknetConv2D_BN_Leaky(num_filters//2, (1,1)),
                DarknetConv2D_BN_Leaky(num_filters, (3,3)))(x)
        x = Add()([x,y])
    return x
```
Resblock_body 由一个zero padding与Conv2D_BN_Leaky，再加上若干个Res_unit，代码如下：
```python
def resblock_body(x, num_filters, num_blocks):
    '''A series of resblocks starting with a downsampling Convolution2D'''
    # Darknet uses left and top padding instead of 'same' mode
    x = ZeroPadding2D(((1,0),(1,0)))(x)
    x = DarknetConv2D_BN_Leaky(num_filters, (3,3), strides=(2,2))(x)
    for i in range(num_blocks):
        y = compose(
                DarknetConv2D_BN_Leaky(num_filters//2, (1,1)),
                DarknetConv2D_BN_Leaky(num_filters, (3,3)))(x)
        x = Add()([x,y])
    return x
```
下面是YOLO网络的主体部分：
```python
def darknet_body(x):
    '''Darknent body having 52 Convolution2D layers'''
    x = DarknetConv2D_BN_Leaky(32, (3,3))(x)
    x = resblock_body(x, 64, 1)
    x = resblock_body(x, 128, 2)
    x = resblock_body(x, 256, 8)
    x = resblock_body(x, 512, 8)
    x = resblock_body(x, 1024, 4)
    return x
```
在res4右边的部分的代码如下，主要就是拼接13，26，52像素图像,由于YOLO是一个多输出的网络结构，需要将输出的layer的序号提取出来，构成输出，这里输出的layer序号就是152,92，以及最后一层： 
 
```python
#注意，13，26，52像素的特征图都需要make_last_layers这个函数，整体来说，完成了
def make_last_layers(x, num_filters, out_filters):
    '''6 Conv2D_BN_Leaky layers followed by a Conv2D_linear layer'''
    x = compose(
            DarknetConv2D_BN_Leaky(num_filters, (1,1)),
            DarknetConv2D_BN_Leaky(num_filters*2, (3,3)),
            DarknetConv2D_BN_Leaky(num_filters, (1,1)),
            DarknetConv2D_BN_Leaky(num_filters*2, (3,3)),
            DarknetConv2D_BN_Leaky(num_filters, (1,1)))(x)
    y = compose(
            DarknetConv2D_BN_Leaky(num_filters*2, (3,3)),
            DarknetConv2D(out_filters, (1,1)))(x)
    return x, y
 
 
def yolo_body(inputs, num_anchors, num_classes):
    """Create YOLO_V3 model CNN body in Keras."""
    # 对于Model对象，初始化时候u，第一个参数是输入，第二个参数是输出
    # 所以相当于建立了一个dark_body 网络
    darknet = Model(inputs, darknet_body(inputs))
    x, y1 = make_last_layers(darknet.output, 512, num_anchors*(num_classes+5))
 
    x = compose(
            DarknetConv2D_BN_Leaky(256, (1,1)),
            UpSampling2D(2))(x)
    x = Concatenate()([x,darknet.layers[152].output])
    x, y2 = make_last_layers(x, 256, num_anchors*(num_classes+5))
 
    x = compose(
            DarknetConv2D_BN_Leaky(128, (1,1)),
            UpSampling2D(2))(x)
    x = Concatenate()([x,darknet.layers[92].output])
    x, y3 = make_last_layers(x, 128, num_anchors*(num_classes+5))
 
    return Model(inputs, [y1,y2,y3])
```
下面是输出计算结果，整体来说，输出了一个向量，这个是需要进行结果拆分的。
 
 
这时输出的内容是
YOLO会抽取13X13，26X26，52X52这三个尺寸的特征图。后面的部分非常的复杂，YOLO的keras实现的作者用了将不同功能切分到不同的模块中，首先看一下，主函数：
```python
def yolo_eval(yolo_outputs,
              anchors,
              num_classes,
              image_shape,
              max_boxes=20,
              score_threshold=.6,
              iou_threshold=.5):
    """Evaluate YOLO model on given input and return filtered boxes."""
    #num_layer 相当于是输出的个数，YOLO是一个但输入，多输出的网络。YOLOv3输出是3
    num_layers = len(yolo_outputs)
    #指定anchor的mask，对应之前指定的
    anchor_mask = [[6,7,8], [3,4,5], [0,1,2]] if num_layers==3 else [[3,4,5], [1,2,3]] # default setting
    # 16X32=416
    input_shape = K.shape(yolo_outputs[0])[1:3] * 32
    boxes = []
    box_scores = []
    #注意下面是在遍历整个layer
    for l in range(num_layers):
        _boxes, _box_scores = yolo_boxes_and_scores(yolo_outputs[l],
            anchors[anchor_mask[l]], num_classes, input_shape, image_shape)
        boxes.append(_boxes)
        box_scores.append(_box_scores)
    #从for循环输出的boxes是一个元组，用concatenate展平一个元素，这个元素n行4列（boxes）
    boxes = K.concatenate(boxes, axis=0)
    #从for循环输出的boxes是一个元组，用concatenate展平一个元素，这个元素n行40列（boxes）
    box_scores = K.concatenate(box_scores, axis=0)
    #将置信度不达标的框去掉
    mask = box_scores >= score_threshold
    #在一个图片中，同一类物体最多有多少个
    max_boxes_tensor = K.constant(max_boxes, dtype='int32')
    boxes_ = []
    scores_ = []
    classes_ = []
    #对每一个class进行处理
    for c in range(num_classes):
        # TODO: use keras backend instead of tf.
        class_boxes = tf.boolean_mask(boxes, mask[:, c])
        class_box_scores = tf.boolean_mask(box_scores[:, c], mask[:, c])
        #进行最大值抑制操作，相当于就是聚类算法，用于清除重复的框
        nms_index = tf.image.non_max_suppression(
            class_boxes, class_box_scores, max_boxes_tensor, iou_threshold=iou_threshold)
 
        class_boxes = K.gather(class_boxes, nms_index)
        class_box_scores = K.gather(class_box_scores, nms_index)
 
        classes = K.ones_like(class_box_scores, 'int32') * c
        boxes_.append(class_boxes)
        scores_.append(class_box_scores)
        classes_.append(classes)
    #同样需要一次拼接
    boxes_ = K.concatenate(boxes_, axis=0)
    scores_ = K.concatenate(scores_, axis=0)
    classes_ = K.concatenate(classes_, axis=0)
 
    return boxes_, scores_, classes_
```
上述代码中比较难以理解的是 yolo_boxes_and_scores。 这个函数，这个函数主要用于提取候选框，给出给一个候选框的类型概率，置信度，width + height + center_x + center_y 这些信息，tf.image.non_max_suppression函数完成了类似Kmean聚类的功能。在输出之前先减少候选框的数量。  
还有要注意的是YOLO的主体输出是三个，在for c in range(num_classes): 中分别进行处理，然后用concatenate 拼接结果。 
下面是比较难理解的yolo_boxes_and_scores， yolo_boxes_and_scores依托两个函数进行，一个是yolo_head这个函数是从YOLO网络中输出候选框的boxes，classes信息等，注意该函数输出的归一化的x,y,w,h坐标。
```python
def yolo_head(feats, anchors, num_classes, input_shape, calc_loss=False):
    """Convert final layer features to bounding box parameters."""
    num_anchors = len(anchors)
    # Reshape to batch, height, width, num_anchors, box_params.
    anchors_tensor = K.reshape(K.constant(anchors), [1, 1, 1, num_anchors, 2])
    # yolo_head 会运行3次，依次将16X16,32X32,64X64的输出进行处理
    grid_shape = K.shape(feats)[1:3] # height, width
    #以16X16特征图输出为例
    #数组内容为 0:1:2--15，第一层嵌套之后为 16,1,1,1
    #tile将数组进一步扩充为 16,16,1,1
    grid_y = K.tile(K.reshape(K.arange(0, stop=grid_shape[0]), [-1, 1, 1, 1]),
        [1, grid_shape[1], 1, 1])
    grid_x = K.tile(K.reshape(K.arange(0, stop=grid_shape[1]), [1, -1, 1, 1]),
        [grid_shape[0], 1, 1, 1])
    #grid成为 16，16,1,1的变量
 
    grid = K.concatenate([grid_x, grid_y])
    grid = K.cast(grid, K.dtype(feats))
 
    feats = K.reshape(
        feats, [-1, grid_shape[0], grid_shape[1], num_anchors, num_classes + 5])
 
    # Adjust preditions to each spatial grid point and anchor size.
    # 神经网络输出的是以网格自身坐标系下的location，需要全局坐标系，这里需要平移网格到对应的位置
    box_xy = (K.sigmoid(feats[..., :2]) + grid) / K.cast(grid_shape[::-1], K.dtype(feats))
    # 将wh取出来，进行处理乘以anchor box的大小，然后就是最终的大小了
    box_wh = K.exp(feats[..., 2:4]) * anchors_tensor / K.cast(input_shape[::-1], K.dtype(feats))
    #将置信度取出来
    box_confidence = K.sigmoid(feats[..., 4:5])
    #将每一种物体的概率取出来
    box_class_probs = K.sigmoid(feats[..., 5:])
 
    if calc_loss == True:
        return grid, feats, box_xy, box_wh
    return box_xy, box_wh, box_confidence, box_class_probs
```
一个是yolo_correct_boxes，这个用于将**归一化的**x,y,w,h 归一化到实际的图片中。 
```python
def yolo_boxes_and_scores(feats, anchors, num_classes, input_shape, image_shape):
    '''Process Conv layer output'''
    box_xy, box_wh, box_confidence, box_class_probs = yolo_head(feats,
        anchors, num_classes, input_shape)
    boxes = yolo_correct_boxes(box_xy, box_wh, input_shape, image_shape)
    boxes = K.reshape(boxes, [-1, 4])
    box_scores = box_confidence * box_class_probs
    box_scores = K.reshape(box_scores, [-1, num_classes])
    #将每一个grid里面对应的box与scores都取出出来，行数应该是所有的box的行数
    return boxes, box_scores
```
