import tensorflow as tf

x1 = tf.constant([1., 2., 3.], dtype=tf.float64)
print("x1:", x1)
#强制tensor转换为该数据类型 tf.cast(张量名,dtype=数据类型)
x2 = tf.cast(x1, tf.int32)
print("x2", x2)
print("minimum of x2：", tf.reduce_min(x2)) #计算张量维度省元素的最小值 tf.reduce_min(张量名)
print("maxmum of x2:", tf.reduce_max(x2)) #计算张量维度省元素的最大值 tf.reduce_max(张量名)
