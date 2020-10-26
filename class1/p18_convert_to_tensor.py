import tensorflow as tf
import numpy as np

a = np.arange(0, 5)
#将numpy的数据类型转换为Tensor数据类型
#tf.convert_to_tensor(数据名,dtype=数据类型(可选))
b = tf.convert_to_tensor(a, dtype=tf.int64)
print("a:", a)
print("b:", b)
