import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#İki değişkenli fonksiyonları, yani z = f(x, y) tipindeki matematiksel ifadeleri görselleştirmek için kullanılır.

x = np.linspace(-3, 3, 600)
y = np.linspace(-3, 3, 600)

#Bu grafikler çizilmeden önce mutlaka bir taban ızgarası (grid) oluşturulmalıdır. Bunun için np.meshgrid fonksiyonu kullanılır.
X, Y = np.meshgrid(x, y)

Z = np.exp(-(X**2 + Y**2))

fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(111, projection="3d")

#surface plotu surface variableina atadık. colormap(cmap) olarak da viridisi belirledik!
surface = ax.plot_surface(X, Y, Z, cmap="viridis")

ax.set_title("3D Surface Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

fig.colorbar(surface, shrink=0.8)

plt.show()