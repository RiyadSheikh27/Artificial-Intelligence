#Inverse matric holo A^-1.. Etar formula holo---If the values is [[1,2],[3,4]] >1/[A]*[[4 -2],[-3 1]]---->Katay likhle bujha jabe
#Power matrix holo--->A^2 = A*A
import numpy as np

var1 = np.matrix([[1, 2], [3,4]])
var2 = np.matrix([[1, 2], [3,4]])

print(np.linalg.inv(var1))
print()
print(np.linalg.matrix_power(var1,2))

