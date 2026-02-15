import numpy as np
from numpy.matrixlib.defmatrix import matrix

matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([10,10,10])

result = matrix + vector
print(result)