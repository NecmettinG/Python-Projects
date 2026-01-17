import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

t = np.linspace(0,20, 2000)

x = np.exp(-0.2 * t) * np.sin(5 * t)

fig, axes = plt.subplots(3, 1, figsize=(8,6))

#color yerine direkt 'r' falan yazabiliyoruz. renk olarak red oluyormus.
axes[0].plot(t, x, color="red")
axes[0].set_title("time response")

axes[1].plot(t, np.exp(-0.2 * t), color="orange")
axes[1].set_title("envelope")

mask = (t >= 0) & (t <= 2)

axes[2].plot(t[mask], x[mask], color="green")
axes[2].set_title("zoomed time response [0,2]")

plt.tight_layout()

plt.show()