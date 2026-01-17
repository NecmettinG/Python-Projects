import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#Use a grid of 40 x 40 points.
x = np.linspace(-4, 4, 40)
y = np.linspace(-4, 4, 40)

#Bu tarz plotlarda mecbur meshgrid(x,y) kullanacaz gibi.
X, Y = np.meshgrid(x, y)

Z = np.sin(X) * np.cos(Y)

fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(111, projection="3d")

#Wireframe plot için plot_wireframe() kullanmamız lazım!
ax.plot_wireframe(X, Y, Z, color="red")

ax.set_title("3D Wireframe Plot of sin(x) * cos(y)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")


plt.show()