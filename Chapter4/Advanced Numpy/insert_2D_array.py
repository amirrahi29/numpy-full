import numpy as np

from Chapter2.Shape import arr_2D

arr_2D = np.array([[1,2,3],[4,5,6]])
print(arr_2D)

new_arr_2D = np.insert(arr_2D,1,[9,8,7],axis=0)
print(new_arr_2D)