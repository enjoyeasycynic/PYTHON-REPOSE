import tensorflow as tf
import numpy as np
#生成训练数据
x_data = np.random.rand(100).astype(np.float32) #产生随机的100个数
y_data = x_data*0.1+0.3 #随机数之间的关系
#stucture start
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0)) #规定第一个系数的范围
biases = tf.Variable(tf.zeros([1])) #规定第二系数的范围

y=Weights*x_data+biases #系数的关系

loss = tf.reduce_mean(tf.square(y-y_data)) #产生loss 减少计算Y的值和实际Y值的差
optimiazer = tf.train.GradientDescentOptimizer(0.5) #优化器，0.5学习效率（0-1）
train = optimiazer.minimize(loss) #优化器 来减少loss

init = tf.initialize_all_variables()#启动器
#end

sess = tf.Session()#初始化
sess.run(init)#指针激活程序

for step in range(201):
sess.run(train)
if step%20==0:
print(step,sess.run(Weights),sess.run(biases))
