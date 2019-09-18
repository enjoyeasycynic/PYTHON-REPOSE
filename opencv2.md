#### 9.1 获取并修改像素值
```python
import cv2
import numpy as np

img=cv2.imread('messi5.jpg') #读入图片
px=img[100,100]#让px等于图片中坐标100，100像素点的信息
print(px)  #[ 72  94 106]
blue=img[100,100,0] #获取BGR（blue，green，red）三通道中的蓝色通道数据
print(blue) #72

px = [255,255,255]
print(px)#让img[100,100]的三通道数值修改为255，255，255
```

#### 9.2 获取图像属性
```
import cv2
import numpy as np
img=cv2.imread('test.bmp')
print(img.shape)
#(480, 752, 3)

import cv2
import numpy as np
img=cv2.imread('test.bmp')
print(img.size, img.dtype) # 返回的是图像的数据类型.

#1082880 uint8
```

#### 9.3 ROI 感兴趣
```
import cv2
import numpy as np
img=cv2.imread('test.bmp')
box=img[280:340,330:390]   #像素横：280-340（60），纵330-390（60）这个60x60的像素片段作为box
img[273:333,100:160]=box   #修改273-333，100-160的像素为box，就是把box的60x60的像素转移到（273-330，100-160）的位置
img=cv2.imshow('test', img)
cv2.waitKey(0)
```

#### 9.4 拆分及合并图像通道
