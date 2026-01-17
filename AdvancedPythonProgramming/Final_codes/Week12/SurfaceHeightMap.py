import matplotlib.pyplot as plt
import numpy as np

#𝑧=sin (𝑥)cos (𝑦) gibi 3 boyutlu bir fonksiyonun tepe ve çukurlarını, 2 boyutlu düzlemde izohips eğrileri ile gösterir.
#Contour Plotta kesinlikle X, Y = np.meshgrid(x, y) kullan!!!

x = np.linspace(-np.pi, np.pi, 200)
y = np.linspace(-np.pi, np.pi, 200)

#np.meshgrid(x, y) → Düzlemi küçük karelere böler.
X, Y = np.meshgrid(x, y)

Z = np.sin(X) * np.cos(Y)

#Çizgilerin yakınlığı dikliği, uzaklığı ise düzlüğü temsil eder.
plt.contour(X, Y, Z, levels=60)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Height Map Contour")
plt.show()