import numpy as np

var = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(var)
print(var.ndim)

print()

x=var.reshape(2,3,2)
print(x)
print("Dimention is :",x.ndim)

print()

x1=var.reshape(-1)
print(x1)
print("Dimention is :",x1.ndim)

