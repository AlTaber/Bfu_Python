import numpy as np

data = np.random.randn(10, 4)

min_value = np.min(data)
max_value = np.max(data)
mean_value = np.mean(data)
std_dev = np.std(data)
first_five_rows = data[:5]

print("Макс:", min_value)
print("Мин:", max_value)
print("Сред:", mean_value)
print("Отклонение:", std_dev)
print("Первые 5 строк:\n", first_five_rows)