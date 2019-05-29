import tensorflow as tf
a = tf.constant(2,name="input_a")
b = tf.constant(4,name="input_b")
c = tf.multiply(a,b,name="mul_c")
d = tf.add(a,b,name="add_d")
e = tf.add(c,d,name="add_e")
sess = tf.Session()
output = sess.run(e)
print(output)
writer = tf.summary.FileWriter('home/feigu/tmp',sess.graph)
writer.close()
sess.close()
#执行完程序后 在终端输入：tensorboard --logdir="home/feigu/tmp"
#根据提示打开http://localhost:6006,进入可视化的数据流图
