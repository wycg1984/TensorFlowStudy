import tensorflow as tf

#理解axis
#在一个二维张量或数组中，可以通过调整axis定于0或1控制执行维度
#axis=0代表跨行(经度,down)即对第一个维度进行操作,而axis=1代表跨列(纬度,across)即对第二维度进行操作
#如果不指定axis，则所有元素参与计算

x = tf.constant([[1, 2, 3], [2, 2, 3]])
print("x:", x)
print("mean of x:", tf.reduce_mean(x))  # 求x中所有数的均值 计算张量沿着指定维度的平均值 tf.reduce_mean(张量名,axis=操作轴)
print("sum of x:", tf.reduce_sum(x, axis=1))  # 求每一行的和 计算张量沿着指定维度的和 tf.reduce_sum(张量名,axis=操作轴 )
