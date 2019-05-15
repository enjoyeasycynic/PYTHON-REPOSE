#### Numpy

- NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的**维度数组与矩阵运算**，此外也针对数组运算提供大量的数学函数库。
- 通常与 SciPy（Scientific Python）和 Matplotlib（绘图库）一起使用
- [详细内容打开](http://www.runoob.com/numpy/numpy-tutorial.html)

##### 基础
##### 1.0 引入
```python
# 引入Numpy
import numpy as np
```
##### 1.1 ndarray 对象
```python
numpy.array(object, dtype =  None, copy =  True, order =  None, subok =  False, ndmin =  0)
```
- object 数组或嵌套的数列

*一维*
```python
import  numpy  as  np
a = np.array([1,2,3])
print  (a)
```
*二维*
```python
import  numpy  as  np
a = np.array([[1, 2], [3, 4]])
print  (a)
```
- dtype  数组元素的数据类型（可选）
```python
# dtype 参数 
import  numpy  as  np
a = np.array([1, 2, 3], dtype = complex)
#complex 是复数
print(a)
```
输出：
```
[1.+0.j,  2.+0.j,  3.+0.j]
```
- copy 对象是否需要复制（可选）
- order 创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
- subok 默认返回一个与基类类型一致的数组
- ndmin 指定生成数组的最小维度
##### 1.2 数据类型
基本上可以和 C 语言的数据类型对应
##### 1.3 numpy 属性
- ndarray.ndim    秩，即轴的数量或维度的数量
```python
import  numpy  as  np  
a = np.arange(24)  
print  (a.ndim)
#结果：1
```
- ndarray.shape   数组的维度，对于矩阵，返回n 行 m 列，.reshape可调节数组大小
```python
import  numpy  as  np
a = np.array([[1,2,3],[4,5,6]])
print  (a.shape)
#结果：(2,  3)
```
- ndarray.size 数组元素的总个数，相当于 .shape 中 n*m 的值
- ndarray.dtype  ndarray 对象的元素类型 
- ndarray.itemsize  ndarray 对象中每个元素的大小，以字节为单位 
- ndarray.flags  ndarray 对象的内存信息 
```
import  numpy  as  np  
x = np.array([1,2,3,4,5])  
print  (x.flags)
```

结果：
```
C_CONTIGUOUS :  True 
F_CONTIGUOUS :  True
OWNDATA :  True
WRITEABLE :  True #数据区域可以被写入，将该值设置为 False，则数据为只读
ALIGNED :  True
WRITEBACKIFCOPY :  False
UPDATEIFCOPY :  False
```
- ndarray.real  ndarray元素的实部 
- ndarray.imag  ndarray 元素的虚部 
- ndarray.data  包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。

##### 1.4 创建数组
- numpy.empty
```python
numpy.empty(shape, dtype =  float, order =  'C')
#shape 数组形状:[3,2]
#order 有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。
```
```
import  numpy  as  np  
x = np.empty([3,2], dtype = int)  
print  (x)
#结果的数组元素为随机值，因为它们未初始化。
```
- numpy.zeros
创建指定大小的数组，数组元素以 0 来填充

```python
import numpy as np
 
# 默认为浮点数
x = np.zeros(5) 
print(x)
 
# 设置类型为整数
y = np.zeros((5,), dtype = np.int) 
print(y)
 
# 自定义类型
z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
print(z)
```
输出：

```
[0.  0.  0.  0.  0.]  
[0  0  0  0  0]  
[[(0,  0)  (0,  0)]  [(0,  0)  (0,  0)]]
```

- numpy.ones
与numpy.zeros对应，默认填充1
#### 索引

##### 3.1 切片
我们也可以通过冒号分隔切片参数**start，(:)stop，(:)tep**来进行切片操作
```
import  numpy  as  np  
a = np.arange(10)  
b = a[2:7:2]  # 从索引 2 开始到索引 7 停止，间隔为 2  
print(b)
```
```
x = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print (x)
print ("x column 1: ", x[:, 1]) #结果第四行 取每个元组中位置为1的元素,位置为1，就是第二个，从0开始计算。
print ("x row 0: ", x[0, :]) #取第一个元组
print ("x rows 0,1,2 & cols 1,2: \n", x[:3, 1:3])
```
结果：
```
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
x column 1:  [ 2  6 10]
x row 0:  [1 2 3 4]
x rows 0,1,2 & cols 1,2: 
 [[ 2  3]
 [ 6  7]
 [10 11]]
 ```
 ##### 3.2 索引
 ```
# 索引 (Indexing)
x = np.array([1, 2, 3])
print ("x[0]: ", x[0])
x[0] = 0
print ("x: ", x)
```
布尔数值索引
```
x = np.array([[1,2], [3, 4], [5, 6]])
print ("x:\n", x)
print ("x > 2:\n", x > 2)
print ("x[x > 2]:\n", x[x > 2]) #打印大于2的元素
```

结果
```
x:
 [[1 2]
 [3 4]
 [5 6]]
x > 2:
 [[False False]
 [ True  True]
 [ True  True]]
x[x > 2]:
 [3 4 5 6]
 ```
 ##### 4.1 基本运算
```
x = np.array([[1,2], [3,4]], dtype=np.float64)
y = np.array([[1,3], [2,5]], dtype=np.float64)
print("x + y:\n", np.add(x, y)) # 加
print("x - y:\n", np.subtract(x, y)) # 减
print("x * y:\n", np.multiply(x, y)) # 乘
```
结果：
```
x + y:
 [[2\. 5.]
 [5\. 9.]]
x - y:
 [[ 0\. -1.]
 [ 1\. -1.]]
x * y:
 [[ 1\.  6.]
 [ 6\. 20.]]
```
##### 4.2 点乘
```
print(x.dot(y))
```

结果
```
[[ 5\. 13.]
 [11\. 29.]]</pre>
```
##### 4.3 跨维度求和
```
x = np.array([[1,2],[3,4]])
print(x)
print("sum all: ", np.sum(x)) # 将所有元素相加
print("sum by col: ", np.sum(x, axis=0)) # 将每列的元素相加
print("sum by row: ", np.sum(x, axis=1)) # 将每行的元素相加
```

结果：
```
[[1 2]
 [3 4]]
sum all:  10
sum by col:  [4 6]
sum by row:  [3 7]
```
##### 4.4转置
```
print("x:\n", x)
print("x.T:\n", x.T)
#结果：
>x:
 [[1 2]
 [3 4]]
x.T:
 [[1 3]
 [2 4]]
 ```

#### 数组高级操作
