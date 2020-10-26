import tensorflow as tf
#设定参数w的随机初始值为5
w = tf.Variable(tf.constant(5, dtype=tf.float32)) #tf.Variable()将变量标记为"可训练"，被标记的变量会在反向传播中记录梯度信息。神经网络训练中，常用该函数标记待训练参数 tf.Variable(初始值)
lr = 0.2  #学习率lr
epoch = 40 #循环迭代40次

for epoch in range(epoch):  # for epoch 定义顶层循环，表示对数据集循环epoch次，此例数据集数据仅有1个w,初始化时候constant赋值为5，循环40次迭代。
    with tf.GradientTape() as tape:  # with结构到grads框起了梯度的计算过程。 用with结构让损失函数的loss对参数w求梯度
        loss = tf.square(w + 1) #损失函数的loss定义为(w+1)^2
    grads = tape.gradient(loss, w)  # .gradient函数告知谁对谁求导

    w.assign_sub(lr * grads)  # .assign_sub 对变量做自减 即：w -= lr*grads 即 w = w - lr*grads(梯度值)
    #打印出每次训练后的参数w和损失函数loss
    print("After %s epoch,w is %f,loss is %f" % (epoch, w.numpy(), loss))

# lr初始值：0.2   请自改学习率  0.001  0.999 看收敛过程
# 最终目的：找到 loss 最小 即 w = -1 的最优参数w
