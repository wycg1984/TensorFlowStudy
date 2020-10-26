import tensorflow as tf
import numpy as np

SEED = 23455

rdm = np.random.RandomState(seed=SEED)  # 生成[0,1)之间的随机数
x = rdm.rand(32, 2) #生成32行2列的输入特征x
y_ = [[x1 + x2 + (rdm.rand() / 10.0 - 0.05)] for (x1, x2) in x]  # 生成噪声[0,1)/10=[0,0.1); [0,0.1)-0.05=[-0.05,0.05)
x = tf.cast(x, dtype=tf.float32) #x转变数据类型

w1 = tf.Variable(tf.random.normal([2, 1], stddev=1, seed=1)) #随机初始化参数w1 初始化为2行1列的随机数

epoch = 15000 #数据集迭代15000次
lr = 0.002 #学习率

#for循环中用with结构 求前向传播计算结果y 求均方误差损失函数loss_mse
for epoch in range(epoch):
    with tf.GradientTape() as tape:
        y = tf.matmul(x, w1)
        loss_mse = tf.reduce_mean(tf.square(y_ - y)) #均方误差
    #损失函数对待训练参数w1求偏导
    grads = tape.gradient(loss_mse, w1)
    #更新参数w1
    w1.assign_sub(lr * grads)
    #每迭代500轮数据 打印当前的参数w1
    if epoch % 500 == 0:
        print("After %d training steps,w1 is " % (epoch))
        print(w1.numpy(), "\n")
print("Final w1 is: ", w1.numpy())
