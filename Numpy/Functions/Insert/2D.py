import numpy as np

var1 = np.array([[1,2],[3,4]])
x = np.insert(var1,2,10,axis=0)
var2 = np.array([[1,2],[3,4]])
x = np.insert(var2,2,[10,20],axis=1)
print(x)