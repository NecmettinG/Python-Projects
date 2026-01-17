import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0, 10, 600)

X = np.sin(t)
Y = np.sin(2*t)
Z = np.sin(3*t)

fig = plt.figure(figsize=(7,5))

#projection='3d' → 3 boyutlu çizimi aktif eder. Olmazsa grafik 2D olur.
ax = fig.add_subplot(111, projection="3d")

ax.plot3D(X, Y, Z, color="red")

ax.set_title("3D Lissajous Curve")
ax.set_xlabel("sin(t)")
ax.set_ylabel("sin(2t)")
ax.set_zlabel("sin(3t)")

ax.grid(True)

#Optional: change viewing angle:
#elev → yukarıdan bakış açısı
#azim → yatay dönüş açısı
#Aynı veri, farklı açılardan farklı algılanır
ax.view_init(elev=20, azim=40)

plt.show()