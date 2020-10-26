import tensorflow as tf
#生成正态分布的随机数，默认均值为0，标准差为1  tf.random.normal(维度, mean=均值, stddev=标准差)
d = tf.random.normal([2, 2], mean=0.5, stddev=1)
print("d:", d)
#生成截断式正态分布的随机数 tf.random.truncated_normal(维度, mean=均值, stddev=标准差)
e = tf.random.truncated_normal([2, 2], mean=0.5, stddev=1) #生成2行2列的张量
print("e:", e)
