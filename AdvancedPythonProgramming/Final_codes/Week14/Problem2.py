import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

t = np.linspace(0, 100, 1000)

u = 40 + 15 * np.sin(0.4 * t) + 8 * np.cos(0.1 * t)

fig, ax = plt.subplots(figsize=(8,6))

ax.plot(t, u, linewidth=3)
ax.set_title("Cpu utilization")

ax_inset = inset_axes(ax, width="35%", height="35%", loc="upper right")

mask = (t >= 30) & (t <= 50)

ax_inset.plot(t[mask], u[mask])
ax_inset.set_title("Zoom 30-50")

plt.show()