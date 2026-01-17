import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0, 6*np.pi, 500)

X = np.cos(t)
Y = np.sin(t)
Z = t

#Önce figure instance oluştur!
fig = plt.figure(figsize=(7,5))

#Daha sonra figure instance ile add_subplot(111, projection="3d") methodunu kullan!
ax = fig.add_subplot(111, projection="3d")

#3D lineplotu çiz.
#ax.plot3D(X, Y, Z) fonksiyonunu kullanarak üç koordinatı aynı anda tanımlamalıyız.
ax.plot3D(X, Y, Z, color="red", linewidth=2)

ax.set_title("3D Lineplot example")
ax.set_xlabel("cos(t)")
ax.set_ylabel("sin(t)")
ax.set_zlabel("t")

ax.grid(True)
plt.show()