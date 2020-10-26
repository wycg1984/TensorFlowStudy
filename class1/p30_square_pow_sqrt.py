import tensorflow as tf

a = tf.fill([1, 2], 3.)
print("a:", a)
print("a的平方:", tf.pow(a, 3)) #次方 tf.pow(张量名, n次方数)
print("a的平方:", tf.square(a)) #平方 tf.square(张量名)
print("a的开方:", tf.sqrt(a)) #开方 tf.sqrt(张量名)
