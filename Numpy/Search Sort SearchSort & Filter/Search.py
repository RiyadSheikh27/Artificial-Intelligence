import numpy as np

var = np.array([1,2,3,4,2,6,7,2])
x1 = np.where(var ==2)
x2 = np.where(var%2 ==0)
print(x1)
print()
print(x2)