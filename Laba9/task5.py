import numpy as np
from scipy.stats import multivariate_normal
import time

def log_density(X, m, C):
    N, D = X.shape
    inv_C = np.linalg.inv(C)
    det_C = np.linalg.det(C)
    
    if det_C <= 0:
        raise Exception("Ковариационная матрица должна быть положительно определенной")

    log_det_C = np.log(det_C)
    norm_const = -0.5 * (D * np.log(2 * np.pi) + log_det_C)
    
    diff = X - m
    result = norm_const - 0.5 * np.sum(diff @ inv_C * diff, axis=1)
    
    return result

N = 1000
D = 2

np.random.seed(42)
m = np.array([0, 0])
C = np.array([[1, 0.5],
              [0.5, 1]])
X = np.random.multivariate_normal(m, C, size=N)

start_time = time.time()
log_density_custom = log_density(X, m, C)
custom_time = time.time() - start_time

start_time = time.time()
log_density_scipy = multivariate_normal(m, C).logpdf(X)
scipy_time = time.time() - start_time

print(f"Время выполнения log_density: {custom_time:.6f} секунд")
print(f"Время выполнения scipy функции: {scipy_time:.6f} секунд")
print(f"Корректность: {np.allclose(log_density_custom, log_density_scipy)}")