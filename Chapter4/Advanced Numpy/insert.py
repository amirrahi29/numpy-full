"""
np.insert(array,index,value,axis=None)
array = original array
index =
value =
axis =
axis = 0, row wise
       1, column wise
"""

import numpy as np

arr = np.array([1,2,3,4,5,6]);
print(np.insert(arr,1,10,0))