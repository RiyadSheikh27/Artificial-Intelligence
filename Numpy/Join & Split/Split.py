import numpy as np

var1 = np.array([1,2,3,4,5,6])
split_arr1 = np.array_split(var1,3)
print(split_arr1)
print()
var2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
split_arr2 = np.array_split(var2,3,axis=0)
print(split_arr2)