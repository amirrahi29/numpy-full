"""
np.delete(array,index,axis=None)
"""
from operator import index

import numpy as np

arr = np.array([1,2,3,4,5,6])
print(np.delete(arr,index(2),axis=None))