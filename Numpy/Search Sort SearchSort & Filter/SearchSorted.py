import numpy as np

var1 = np.array([1,2,3,4,6,7])
var2 = np.array([1,2,3,7,8,9])
#Kon index e 5 bosano jay
x1 = np.searchsorted(var1 , 5)
#Pura array chaile bosano jabe
x2 = np.searchsorted(var2 , [4,5,6], side='right')
print(x1)
print()
print(x2)
