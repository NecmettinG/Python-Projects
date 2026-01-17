import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-2, 2, 300)
y = np.linspace(-2, 2, 300)

X, Y = np.meshgrid(x, y)

T = np.exp(-(X**2 + Y**2)) * np.cos(2 * X) * np.sin(2 * Y)

#Create subplots
fig = plt.figure(figsize=(14,6))

#Full 3D surface
ax = fig.add_subplot(1,2,1, projection="3d")

surface = ax.plot_surface(X, Y, T, cmap="viridis")

ax.set_title("Temperature Distribution of Metal Plate")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Temperature Distribution T")

#Adding contour graph as well, on z-min
ax.contour(X, Y, T, zdir="z", offset=T.min(), cmap="viridis")

#Zoom domain:
x_zoomed = np.linspace(-1, 1, 150)
y_zoomed = np.linspace(-1, 1, 150)

Xz, Yz = np.meshgrid(x_zoomed, y_zoomed)

Tz = np.exp(-(Xz**2 + Yz**2)) * np.cos(2 * Xz) * np.sin(2 * Yz)

ax2 = fig.add_subplot(1, 2, 2, projection="3d")

ax2.plot_surface(Xz, Yz, Tz, cmap="plasma")

ax2.set_title("Zoomed Surface -1 <= X,Y <=1")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("T")

plt.tight_layout()
plt.show()


