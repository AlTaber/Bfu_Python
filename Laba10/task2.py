import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)
ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]

fig, axes = plt.subplots(2, 2)
axes = axes.flatten()

for ax, (a, b) in zip(axes, ratios):
    x = np.sin(a * t)
    y = np.sin(b * t)
    ax.plot(x, y)
    ax.set_title(f'Лисажу {a}:{b}')
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_xticks([])
    ax.set_yticks([])

fig.suptitle('Фигуры Лисажу с разными соотношениями частот', fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 1])
plt.show()
