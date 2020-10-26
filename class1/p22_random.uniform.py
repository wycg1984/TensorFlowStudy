import tensorflow as tf
#生成均匀分布随机数[minval,maxval] tf.random.uniform(维度, minval=最小值, maxval=最大值)
f = tf.random.uniform([2, 2], minval=0, maxval=1)
print("f:", f)
