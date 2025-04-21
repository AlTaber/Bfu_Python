import numpy as np

matrix = np.loadtxt('laba_9_1.txt', dtype=int, delimiter=',')

print(f"Сумма элементов матрицы: {np.sum(matrix)}")
print(f"Максимальный элемент матрицы: {np.max(matrix)}")
print(f"Минимальный элемент матрицы: {np.min(matrix)}")