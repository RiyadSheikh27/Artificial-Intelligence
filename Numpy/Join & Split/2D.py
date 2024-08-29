import numpy as np

var1 = np.array([[1,2],[3,4]])
var2 = np.array([[5,6],[7,8]])
print(var1)
print()
print(var2)
print()
new_arr = np.concatenate((var1,var2),axis=1)
print(new_arr)
print()

#Concatenate er poriborte stack o use kora jay
new_arr2 = np.stack((var1,var2),axis=1)
print(new_arr2)
print()
#axis use na kore stack er age v/h(vertical/horizontal)use koreo kora jay
new_arr3 = np.hstack((var1,var2))
print(new_arr3)

