"""
np.concatenate((arr1,arr2),axis=0)
np.concatenate((arr1,arr2),axis=1))

axis = 0 (vertical stacking)
axis = 1 (horizontal stacking)
"""


import numpy as np

arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([7,8,9,10,11,12,13])

new_arr = np.concatenate((arr1,arr2), axis=0)

print(new_arr)