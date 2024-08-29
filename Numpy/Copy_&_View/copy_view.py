import numpy as np

var = np.array([1,2,3,4])
co = var.copy()
view = var.view()
var[1]=20
print(co)
print(view)