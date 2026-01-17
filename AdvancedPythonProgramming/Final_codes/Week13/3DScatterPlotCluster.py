import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#Generate Clusters!
np.random.seed(1)

#Cluster A centered at (0,0,0), 300 points
x1 = np.random.normal(0, 1, 300)
y1 = np.random.normal(0, 1, 300)
z1 = np.random.normal(0, 1, 300)

#Cluster B centered at (3,3,3), 300 points
x2 = np.random.normal(3, 1, 300)
y2 = np.random.normal(3, 1, 300)
z2 = np.random.normal(3, 1, 300)

fig = plt.figure(figsize=(7,5))

ax = fig.add_subplot(111, projection="3d")

#Bu arada c yerine color da yazabilirsin.
ax.scatter3D(x1, y1, z1, c="red", alpha=0.7, label="Cluster A")

ax.scatter3D(x2, y2, z2, c="blue", alpha=0.7, label="Cluster B")

ax.set_title("2 Clusters with 3d Scatter")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.grid(True)
#Legend da ekledik!
ax.legend()
plt.show()