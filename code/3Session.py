import tensorflow as tf
matrix1 = tf.constant([[3,3]])#一行两列
matrix2 = tf.constant([[2],[2]])#一列两行
product = tf.matmul(matrix1,matrix2) #矩阵乘法

# sess = tf.Session()
# result = sess.run(product)
# print(result)
# sess.close()

with tf.Session() as sess:
  result2 = sess.run(product)
  print(result2)
