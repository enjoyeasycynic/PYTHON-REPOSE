import tensorflow as tf
#定义变量
state = tf.Variable(0,name='counter')
#print(state.name) #可以打印他的名字
one = tf.constant(1)#常量1

new_value = tf.add(state,one)
update = tf.assign(state,new_value)# 把新的value加载到state上
#此时的state = new_value
#*******important part，有定义变量就需要下面这句
init = tf.initialize_all_variables()#先初始化变量，再用session.run才能激活
#*******
with tf.Session() as sess:
sess.run(init)#激活
for _ in range(3):#3个循环
sess.run(update)#每次运行update
print(sess.run(state))
