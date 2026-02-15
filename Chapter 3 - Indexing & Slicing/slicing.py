"""
slicing
array[start,stop,step]

ar[start:end], start to end -1

negative step, -1 reverse
"""
import numpy as np
arr = np.array([1,2,3,4,5])

print(arr[1:4])
print(arr[:4])
print(arr[::2])
print(arr[::-1])