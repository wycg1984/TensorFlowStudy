import tensorflow as tf
# 独热编码(one-hot encoding)：在分类问题中，常用独热码做标签，标记类别：1表示是，0表示非
classes = 3
labels = tf.constant([1, 0, 2])  # 输入的元素值最小为0，最大为2
output = tf.one_hot(labels, depth=classes) #tf.one_hot()函数将待转换数据，转换为obe-hot形式的数据输出 tf.one_hot(待转换数据,depth=几分类)
print("result of labels1:", output)
print("\n")
