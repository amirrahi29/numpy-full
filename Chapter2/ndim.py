#check which type of dimension type it is like 1D, 2D, 3D

import numpy as np

arr_1D = np.array([1,2,3,4,5])
arr_2D = np.array([[1,2,3],[4,5,6]])
arr_3D = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

print(arr_1D.ndim)
print(arr_2D.ndim)
print(arr_3D.ndim)