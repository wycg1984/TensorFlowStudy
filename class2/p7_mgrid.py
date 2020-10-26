import numpy as np
import tensorflow as tf

# 生成等间隔数值点 np.mgrid[起始值:结束值:步长, 起始值:结束值:步长,...]
x, y = np.mgrid[1:3:1, 2:4:0.5]
# 将x, y拉直，并合并配对为二维张量，生成二维坐标点  x.ravel() 将x变为一维数组 "把.前变量拉直"
# np.c_[] 使返回的间隔数值点配对 np.c_[数组1,数组2,...]
grid = np.c_[x.ravel(), y.ravel()]
print("x:\n", x)
print("y:\n", y)
print("x.ravel():\n", x.ravel())
print("y.ravel():\n", y.ravel())
print('grid:\n', grid)

#
