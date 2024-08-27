import numpy as np

var1 = np.array([1,2,3,4,5])
for i in var1:
    print(i)

print()
var2 = np.array([[1,2,3,4],[5,6,7,8]])
for k in var2:
    for l in k:
       print(l)

print()
var3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
for i in var3:
    for j in i:
        for k in j:
            print(k)