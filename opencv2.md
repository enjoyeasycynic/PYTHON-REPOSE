#### 9.1 获取并修改像素值
```python
import cv2
import numpy as np

img=cv2.imread('messi5.jpg') #读入图片
px=img[100,100]
print(px)
blue=img[100,100,0]
print(blue)
