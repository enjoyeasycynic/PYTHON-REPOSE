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

#### 
