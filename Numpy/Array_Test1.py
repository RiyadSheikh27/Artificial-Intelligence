import numpy as np
# 1D Array
x=np.array([1,2,3,4])
print(x)
print(type(x))
print(x.ndim)
# 2D Array
y=np.array([[1,2,3,4],[1,2,3,4]])
print(y)
print(y.ndim)
# 3D Array
z=np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(z)
print(z.ndim)
# H.Mul.Array
A=np.array([1,2,3,4],ndmin=10)
print(A)
print(A.ndim)