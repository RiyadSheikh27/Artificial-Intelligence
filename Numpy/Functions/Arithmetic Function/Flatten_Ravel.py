import numpy as np

var = np.array([1,2,3,4,5,6])
x = np.resize(var,(2,3))
print(x)
print()
print("Flutten: ",x.flatten(order="F"))
print()
print("Ravel: ",x.ravel(order="F"))
#Order dewa optional, eta diye just row borabor naki colum borabor array output asbe ta bujhay