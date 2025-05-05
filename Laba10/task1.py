import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

x = np.linspace(-1, 1, 500)
fig, ax = plt.subplots(figsize=(8, 6))
colors = plt.cm.viridis(np.linspace(0, 1, 7))

for i, n in enumerate(range(1, 8)):
    Pn = legendre(n)
    y = Pn(x)
    ax.plot(x, y, color=colors[i])
    x_annot = 0.7
    y_annot = Pn(x_annot)
    ax.annotate(f'n = {n}', xy=(x_annot, y_annot), xytext=(10, 0),
                textcoords='offset points', color=colors[i], fontsize=10)

ax.set_title('Полиномы Лежандра')
ax.set_xlabel('x')
ax.set_ylabel('P_n(x)')

ax.grid(True)

plt.tight_layout()
plt.show()
