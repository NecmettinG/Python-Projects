import matplotlib.pyplot as plt
import numpy as np

#Bir fonksiyonun en hızlı artış yönünü (gradyan vektörleri) oklarla gösterir.

x = np.linspace(-3, 3, 20)
y = np.linspace(-3, 3, 20)

#Vector Fieldda (Quiver Plotta) ya Y, X = np.mgrid[-3:3:20j, -3:3:20j] ya da X, Y = np.meshgrid(x, y) kullanacaz!
X, Y = np.meshgrid(x, y)

# f(x, y) (Loss Function) = (x**2) + (y**2) => Vf (Gradient)= (2x, 2y)

U = 2*X
V = 2*Y

#Okların yönü vektör yönünü, uzunluğu vektör büyüklüğünü gösterir.
plt.quiver(X, Y, U, V, color="brown")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Gradient Vector Field")
plt.show()