import numpy as np
var1 = np.array([[1,2,3,4],[1,2,3,4]])
var2 = np.array([[1,2,3,4],[1,2,3,4]])

var = var1+var2
print(var)

print("Min: ",np.min(var),np.argmin(var))
print()
print("max: ",np.max(var),np.argmax(var))
print()
print("Max in x axis: ",np.max(var,axis=0))
print()
print("Sqrt: ",np.sqrt(var))
print()
print("Sin: ",np.sin(var))
print()
print("Cos: ",np.cos(var))
print()
print("Cumsum: ",np.cumsum(var1))
#Hello World