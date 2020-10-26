#第一步：导入相关模块
import tensorflow as tf
from sklearn import datasets
import numpy as np
#第二步：告知要喂入网络的训练集和测试集是什么 即要指定训练集的输入特征x_train和训练集的标签y_train 指定测试集的输入特征x_test和测试集的标签y_test
x_train = datasets.load_iris().data
y_train = datasets.load_iris().target

np.random.seed(116)
np.random.shuffle(x_train)
np.random.seed(116)
np.random.shuffle(y_train)
tf.random.set_seed(116)
#在Sequential()中搭建网络结构 逐层描述每层网络 相当于走了一遍前向传播
#拉直层Flatten() 这一层不含计算只是形状转换， 把输入特征拉直变成一维数组
#全链接层 Dense(神经元个数,activation="激活函数",kernel_regularizer=哪种正则化)
#卷积层 Conv2D(filters=卷积核个数,kernel_size=卷积核尺寸,strides=卷积步长,padding="valid" or "same")
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(3, activation='softmax', kernel_regularizer=tf.keras.regularizers.l2())
])
#第四步：在compile()中配置训练方法 告知训练时选择哪种优化器 选择哪个损失函数 选择哪种评测指标
#compile(optimizer=优化器,loss=损失函数,metrics=["准确率"])
model.compile(optimizer=tf.keras.optimizers.SGD(lr=0.1),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['sparse_categorical_accuracy'])
#第五步：在fit()中执行训练过程 告知训练集和测试集的输入特征和标签 告知每个batch是多少 告知要迭代多少次数据集
#fit(训练集的输入特征,训练集的标签,batch_size= ,epochs=,validation_data=(测试集的输入特征,测试集的标签),validation_split=从训练集划分多少比例给测试集,validation_freq=多少次epoch测试一次)
model.fit(x_train, y_train, batch_size=32, epochs=500, validation_split=0.2, validation_freq=20)
#第六步：用summary()打印出网络的结构和参数统计
model.summary()
