import tensorflow as tf 

m1 = tf.constant([[1.,1.]])
m2 = tf.constant([1.,3.])
r1 = tf.multiply(m1,m2)
#r2 = tf.matmul(m1,m2) 上面m1是一个矩阵元素的矩阵。m2是两个数字元素的矩阵

sess = tf.Session()

print(m1)
print(sess.run(m1))
print("wtf~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(m2)
print(sess.run(m2))
print("wtf~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(sess.run(tf.add(m1,m2)))
print("wtf~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(sess.run(r1))
#print(sess.run(r2))


#结果：
# Tensor("Const:0", shape=(1, 2), dtype=float32)
# [[1. 1.]]
# wtf~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Tensor("Const_1:0", shape=(2,), dtype=float32)
# [1. 3.]
# wtf~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# [[2. 4.]]
# wtf~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# [[1. 3.]]
