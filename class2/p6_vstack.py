import numpy as np
# np.vstack() 将两个数组按垂直方向叠加  np.vstack(数组1，数组2)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.vstack((a, b))
print("c:\n", c)

