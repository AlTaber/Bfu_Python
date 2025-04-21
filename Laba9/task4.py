import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
zero_indexes = np.where(x[:-1] == 0)[0]
candidates = x[zero_indexes + 1]
max_element = candidates.max()

print(max_element)