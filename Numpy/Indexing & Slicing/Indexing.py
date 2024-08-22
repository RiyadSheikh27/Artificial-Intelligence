import numpy as np
var1 = np.array([1,2,3,4])
#Index-           0,1,2,3,4
#or,              -4,-3,-2,-1
print(var1[1])
print(var1[-3])
print()
var2 = np.array([[1,2,3,4],[5,6,7,8]])
print(var2[1,2])
print()
var3 = np.array([[[1,2],[3,4]]])
print(var3[0,1,0])