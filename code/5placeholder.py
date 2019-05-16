import tensorflow as tf 
import numpy as np 
import matplotlib.pyplot as plt

#代码解释相仿于0tensorflow.py，其他不解释

x_data = np.random.randn(100)
y_data = x_data*0.3+0.1
 
weight = tf.Variable(0.5)
bias = tf.Variable(0.5)
#*******************************
x_ = tf.placeholder(tf.float32)
y_ = tf.placeholder(tf.float32)
#这里要解释一下这两个占位符placeholder的作用：
#避免反复地切换底层程序实际运行的上下文
# 所以placeholder()函数是在神经网络构建graph的时候在模型中的占位，此时并没有把要输入的数据传入模型，
# 它只会分配必要的内存。等建立session，在会话中，运行模型的时候通过feed_dict()函数向占位符喂入数据。
#********************************
#所以这里的代码和0tensorflow.py中的些许不一样。
#当输入的数据量特别大时，placeholder的作用尤为明显
#*********************************
#tf.placeholder(
#    dtype,
#    shape=None,
#    name=None)
#dtype：数据类型。常用的是tf.float32,tf.float64等数值类型
#shape：数据形状。默认是None，就是一维值，也可以是多维（比如[2,3], [None, 3]表示列是3，行不定）
#name：名称
#以上
y_modele = weight*x_+bias

loss = tf.pow((y_modele - y_),2)
train = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

sess = tf.Session()
init = tf.initialize_all_variables()
sess.run(init)

for _ in range(10):
    for(x,y) in zip (x_data,y_data):
        sess.run(train,feed_dict={x_:x,y_:y})
    print("weight:",weight.eval(sess),"|bias:",bias.eval(sess))

plt.plot(x_data,y_data,'or',label='original')
plt.plot(x_data,sess.run(weight)*(x_data)+sess.run(bias),label='trained')
plt.legend()
plt.show()
