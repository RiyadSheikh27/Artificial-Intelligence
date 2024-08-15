import numpy as np

var = np.array([1,2,3,4,5,6])
print(var)
print(var.ndim)

print()

x=var.reshape(3,2)
print(x)
print("Dimention is :",x.ndim)



