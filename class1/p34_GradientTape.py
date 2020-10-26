import tensorflow as tf
#with结构记录计算过程，gradient求出张量的梯度
#with tf.Gradient() as tape:
#   若干个计算过程
#grad=tape.gradient(函数,对谁求导)
with tf.GradientTape() as tape:
    x = tf.Variable(tf.constant(3.0))
    y = tf.pow(x, 2)
grad = tape.gradient(y, x)
print(grad)
