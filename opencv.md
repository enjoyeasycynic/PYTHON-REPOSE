# Python-opencv


OPENCV主要参考网站:
[https://www.cnblogs.com/Undo-self-blog/p/8423851.html](https://www.cnblogs.com/Undo-self-blog/p/8423851.html)

#### 1.0 图片视频读写保存
##### 1.1 读入图像
使用函数如下读入图像。 
```python
import numpy as np
import cv2
 
img = cv2.imread('bird.png',cv2.IMREAD_COLOR)
#这里cv2.IMREAD_COLOR可不填
```
 
**cv2.imread参数解释：**  
'bird.png'：
- 给函数提供完整的图片路径 
 
cv2.IMREAD_COLOR（可选）:
- `cv2.IMREAD_COLOR`（默认）：读入一副彩色图像
- `cv2.IMREAD_GRAYSCALE`：以灰度模式读入图像
- `cv2.IMREAD_UNCHANGED`：读入一幅图像，并且包括图像的 alpha 通道  
 
**注意：文件名路径有问题不会报错，但是Show时会不显示或者返回none**
##### 1.2 显示图片
使用函数显示图像。窗口会**自动调整**为图像大小。
```python
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
**cv2.imshow参数解释：** 
'image'：
- 窗口的名字，可以创建多个，但是命名不可以相同  
 
img：
- 图片变量    
 
附录： 
cv2.waitKey() 是一个键盘绑定函数。需要指出的是它的时间尺度是毫秒级。函数等待特定的几毫秒，看是否有键盘输入。特定的几毫秒之内，如果按下任意键，这个函数会返回按键的ASCII码值，程序将会继续运行。如果没有键盘输入，返回值为-1，如果我们设置这个函数的参数为 0，那它将会无限期的等待键盘输入。它也可以被用来检测特定键是否被按下，例如按键a是否被按下，这个后面我们会接着讨论。   
cv2.destroyAllWindows()可以轻易删除任何我们建立的窗口。如果你想删除特定的窗口可以使用cv2.destroyWindow()，在括号内输入你想删除的窗口名。
```
import numpy as np
import cv2

img = cv2.imread('messi5.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
```
按下’s’键保存后退出，或者按下 ESC 键退出不保存。
##### 1.3 保存图像
```python
cv2.imwrite('messigray.png',img)
#cv2.imwrite('文件名及其路径',图像变量名称)
```
##### 1.4 Matplotlib
Matplotib 是 python 的一个绘图库
#### 1.5 用摄像头捕获

OpenCV的简单接口 `VideoCapture` 对象
- ##### 获取视频
```python
cap = cv2.VideoCapture(0)
#一般的笔记本电脑都有内置摄像头。所以参数就是 0。你可以通过设置成 1 或者其他的来选择别的摄像头
cap = cv2.VideoCapture('D:\output.avi')
#也可以用来播放视频
```
- ##### 读入视频
1. `cap.read()` 按帧读取视频，它的返回值有两个：`ret`, `frame`。其中`ret`是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。`frame`就是每一帧的图像，是个三维矩阵。
2. 有时 `cap `可能不能成功的初始化摄像头设备。这种情况下上面的代码会报错。你可以使用 `cap.isOpened()`，来检查是否成功初始化了。如果返回值是True，那就没有问题。否则就要使用函数 `cap.open()`。

- ##### 播放视频
1.  `cv2.imshow('iframe', gray)` 播放视频，第一个参数是视频播放窗口的名称，第二个参数是视频的当前帧。
2.  `cv2.waitKey(25)` 每一帧的播放时间，毫秒级。

- ##### 停止捕获视频
1.  通过外部键盘输入
```
cv2.waitKey(25) & 0xFF == ord('q'):  
    break
```
1.  通过`cap.read()` 的返回值ret，若ret值为False，则停止捕获视频。这种适合读取视频文件时进行判定，通过摄像头录像则只能通过第一种方式停捕获视频。

- ##### 保存视频

1.  `out = cv2.VideoWriter(filePath, fourcc, 800, size)` 设置输出视频的名称，视频的格式，视频的帧速，视频的大小等。
2.  `fourcc = cv2.cv.FOURCC(*'CVID')` 设置要保存视频的格式。
- ##### 释放对象和销毁窗口
```
cap.release()
    out.release()
    cv2.destroyAllWindows()
```
举例：

```
import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')

while(cap.isOpened()):
#你可以使用 cap.isOpened()，来检查是否成功初始化了。如果返回值是True，那就没有问题。

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#将摄像头捕获的视频转换为灰色并且保存
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

#### 1.0 图片视频读写保存
##### 1.1 读入图像
使用函数如下读入图像。 
```python
import numpy as np
import cv2
 
img = cv2.imread('bird.png',cv2.IMREAD_COLOR)
#这里cv2.IMREAD_COLOR可不填
```
 
**cv2.imread参数解释：**  
'bird.png'：
- 给函数提供完整的图片路径 
 
cv2.IMREAD_COLOR（可选）:
- cv2.IMREAD_COLOR（默认）：读入一副彩色图像
- cv2.IMREAD_GRAYSCALE：以灰度模式读入图像
- cv2.IMREAD_UNCHANGED：读入一幅图像，并且包括图像的 alpha 通道  
 
**注意：文件名路径有问题不会报错，但是Show时会不显示或者返回none**
##### 1.2 显示图片
使用函数显示图像。窗口会**自动调整**为图像大小。
```python
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
**cv2.imshow参数解释：** 
'image'：
- 窗口的名字，可以创建多个，但是命名不可以相同  
 
img：
- 图片变量    
 
附录： 
cv2.waitKey() 是一个键盘绑定函数。需要指出的是它的时间尺度是毫秒级。函数等待特定的几毫秒，看是否有键盘输入。特定的几毫秒之内，如果按下任意键，这个函数会返回按键的ASCII码值，程序将会继续运行。如果没有键盘输入，返回值为-1，如果我们设置这个函数的参数为 0，那它将会无限期的等待键盘输入。它也可以被用来检测特定键是否被按下，例如按键a是否被按下，这个后面我们会接着讨论。   
cv2.destroyAllWindows()可以轻易删除任何我们建立的窗口。如果你想删除特定的窗口可以使用cv2.destroyWindow()，在括号内输入你想删除的窗口名。
##### 1.3
 **2.0 生成画布`img`**

```
import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)
```
**2.1 画线**
```
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
```
起点和终点分别是`(0, 0)`，`(511, 511)`，线条颜色为` (255, 0, 0)`，`5`像素粗细。
**2.2 画矩形**
```
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 5)
```
起点和终点分别为`(384, 0)`， `(510, 128)`，矩形颜色为 `(0, 255, 0)`，`5`像素粗细。
**2.3 画圆形**
```
cv2.circle(img, (447, 63), 50, (0, 0, 255),-1)
```
圆点坐标是`(447, 63)`，半径为`50`像素，颜色为`(0, 0, 255)`，`-1`表示圆内部将被用(0, 0, 255)色值填充。
