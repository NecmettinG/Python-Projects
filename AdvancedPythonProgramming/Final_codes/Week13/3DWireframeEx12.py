import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)

X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(111, projection="3d")

ax.plot_wireframe(X, Y, Z, color="red")

ax.set_title("3D Wireframe Plot of (x**2 + y**2)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()