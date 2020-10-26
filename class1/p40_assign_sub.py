import tensorflow as tf

x = tf.Variable(4)
# 赋值操作，更新参数的值并返回
# 调用assign_sub前，先用tf.Variable定义变量w为可训练(可自更新)
# w.assign_sub(w要自减内容)
x.assign_sub(1)
print("x:", x)  # 4-1=3
