import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 2 * np.pi, 1000)
delta = np.pi / 2

frames = 200

fig, ax = plt.subplots()
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal')
ax.grid(True)

line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return (line,)

def update(frame):
    ratio = frame / frames
    a = 1
    b = ratio

    x = np.sin(a * t + delta)
    y = np.sin(b * t)

    line.set_data(x, y)
    ax.set_title(f"Фигура Лисажу: соотношение 1:{ratio:.2f}")
    return (line,)

anim = FuncAnimation(
    fig,
    update,
    frames=frames + 1,
    init_func=init,
    blit=True,
    interval=15
)

plt.show()
