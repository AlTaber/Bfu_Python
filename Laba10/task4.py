import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

t = np.linspace(0, 2 * np.pi, 1000)

init_amp1 = 1.0
init_freq1 = 1.0
init_amp2 = 1.0
init_freq2 = 1.0

def compute_wave(amp, freq):
    return amp * np.sin(freq * t)

# Окно 1
fig1, ax1 = plt.subplots(figsize=(4, 2.25))
plt.subplots_adjust(left=0.2, bottom=0.25)
wave1_line, = ax1.plot(t, compute_wave(init_amp1, init_freq1), lw=2, color='cyan')
ax1.set_title('Волна 1')
ax1.set_xlabel('t')
ax1.set_ylabel('Амплитуда')

axamp1 = plt.axes([0.2, 0.1, 0.65, 0.03])
axfreq1 = plt.axes([0.2, 0.15, 0.65, 0.03])
slider_amp1 = Slider(axamp1, 'Ампл.', 0.0, 5.0, valinit=init_amp1)
slider_freq1 = Slider(axfreq1, 'Част.', 0.1, 10.0, valinit=init_freq1)

# Окно 2
fig2, ax2 = plt.subplots(figsize=(4, 2.25))
plt.subplots_adjust(left=0.2, bottom=0.25)
wave2_line, = ax2.plot(t, compute_wave(init_amp2, init_freq2), lw=2, color='magenta')
ax2.set_title('Волна 2')
ax2.set_xlabel('t')
ax2.set_ylabel('Амплитуда')

axamp2 = plt.axes([0.2, 0.1, 0.65, 0.03])
axfreq2 = plt.axes([0.2, 0.15, 0.65, 0.03])
slider_amp2 = Slider(axamp2, 'Ампл.', 0.0, 5.0, valinit=init_amp2)
slider_freq2 = Slider(axfreq2, 'Част.', 0.1, 10.0, valinit=init_freq2)

# Окно 3
fig3, ax3 = plt.subplots(figsize=(4, 2.25))
sum_line, = ax3.plot(t, compute_wave(init_amp1, init_freq1) + compute_wave(init_amp2, init_freq2), lw=2, color='purple')
ax3.set_title('Сумма волн')
ax3.set_xlabel('t')
ax3.set_ylabel('Амплитуда')

def update(val):
    amp1 = slider_amp1.val
    freq1 = slider_freq1.val
    amp2 = slider_amp2.val
    freq2 = slider_freq2.val

    y1 = compute_wave(amp1, freq1)
    y2 = compute_wave(amp2, freq2)
    ysum = y1 + y2

    wave1_line.set_ydata(y1)
    wave2_line.set_ydata(y2)
    sum_line.set_ydata(ysum)

    fig1.canvas.draw_idle()
    fig2.canvas.draw_idle()
    fig3.canvas.draw_idle()

slider_amp1.on_changed(update)
slider_freq1.on_changed(update)
slider_amp2.on_changed(update)
slider_freq2.on_changed(update)

plt.show()
