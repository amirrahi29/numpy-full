#np.isinf(array) 10*1000
#1/10

import numpy as np

arr = np.array([1,2,np.inf,4,np.inf,5,6])

print(np.isinf(arr))