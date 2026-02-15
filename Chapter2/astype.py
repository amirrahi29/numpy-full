# change data type

import numpy as np

arr = np.array([10,20,30.5,40])
print(arr.dtype)

int_arr = arr.astype(int)

print(int_arr)
print(int_arr.dtype)