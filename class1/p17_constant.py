import tensorflow as tf
#创建一个张量 tf.constant(张量内容,dtype=数据类型(可选))
a = tf.constant([1, 5], dtype=tf.int64)
print("a:", a)
print("a.dtype:", a.dtype) #打印出a的数据类型
print("a.shape:", a.shape) #打印出a的形状

# 本机默认 tf.int32  可去掉dtype试一下 查看默认值
