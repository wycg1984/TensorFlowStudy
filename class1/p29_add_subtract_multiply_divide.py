import tensorflow as tf

a = tf.ones([1, 3])
b = tf.fill([1, 3], 3.)
print("a:", a)
print("b:", b)
print("a+b:", tf.add(a, b))  #加 tf.add(张量1, 张量2)
print("a-b:", tf.subtract(a, b)) #减 tf.subtract(张量1, 张量2)
print("a*b:", tf.multiply(a, b)) #乘 tf.multiply(张量1, 张量2)
print("b/a:", tf.divide(b, a)) #除 tf.divide(张量1, 张量2)
