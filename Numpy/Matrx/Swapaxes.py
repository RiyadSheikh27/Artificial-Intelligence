#Kind of Transpose matric but ekhane kon axis k kon axis e nite hbe mention krte hoy
#Etar mane hocche A^T, mane matrix er ulta. Row jabe colum borabor r colum jabe row borabor
import numpy as np

var1 = np.matrix([[1, 2, 3], [4, 5, 6]])

print(np.swapaxes(var1,0,1))
