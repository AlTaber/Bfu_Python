import numpy as np

def run_length_encoding(x):
    values = np.array([], dtype=x.dtype)
    counts = np.array([], dtype=int)
    
    current_value = x[0]
    count = 0
    for value in x:
        if value == current_value:
            count += 1
        else:
            values = np.append(values, current_value)
            counts = np.append(counts, count)
            current_value = value
            count = 1
    values = np.append(values, current_value)
    counts = np.append(counts, count)
    
    return values, counts

x = np.array([2, 2, 2, 3, 3, 3, 5])
print(run_length_encoding(x))