import numpy as np

var = np.array([1,2,3,2,3,4,5,3,7,8,4,9,3,7])

x = np.unique(var,return_index=True,return_counts=True)
#return_index=True,return_counts=True---->Eta diye index r kotota kore ache data count kre
print(x)