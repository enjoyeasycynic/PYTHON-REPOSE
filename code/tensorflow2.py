import tensorflow as tf
import numpy as np
#引入tensorflow和numpy包
inputX = np.random.rand(300,1)#随机生成输入的线性数
noise = np.random.normal(0,0.5,inputX.shape)#偏差在0.5左右的正态分布噪音数
outputY = inputX*4+1+noise#随机生成的输入Y


#****************************build structure
weight1 = tf.Variable(np.random.rand(inputX.shape[1],4))
bias1 = tf.Variable(np.random.rand(inputX.shape[1],4))
x1 = tf.placeholder(tf.float64,[None,1])
y1_ = tf.matmul(x1,weight1) + bias1
#weight1和bias1都是隐藏层的变量
#x1是palceholder是前面输入的计算数据，而y1_是我们自己设立的
y = tf.placeholder(tf.float64,[None,1])
loss = tf.reduce_mean(tf.reduce_sum(tf.square((y1_ - y)),reduction_indices = [1]))
train = tf.train.GradientDescentOptimizer(0.25).minimize(loss)
#loss定义的函数是损失函数，最小二乘法的损失函数，就是模型输出与真实值之间的误差最小二乘法
#而优化器使用的是梯度下降法
#****************************
init = tf.initialize_all_variables()
#初始化所有变量
sess = tf.Session()
sess.run(init)
#**********开始
for i in range(1000):
        sess.run(train,feed_dict={x1:inputX,y:outputY})
#feed_dict 会把设定值一次传送到训练模型中
print(weight1.eval(sess))
print("-----------------------------------")
print(bias1.eval(sess))
print("-----------------------------------")
x_data = np.matrix([[1.],[2.],[3.]])
print(sess.run(y1_,feed_dict={x1:x_data}))
