import numpy as np

var = np.array([1,2,3,4])
# x = np.insert(var,2,10)-->Evabe Single Value bosano jay ba nicher moto double index eo vaalue bosano jay
x = np.insert(var,(2,4),10)
print(x)