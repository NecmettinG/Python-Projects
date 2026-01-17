import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 300)
y = np.linspace(-3, 3, 300)

#np.meshgrid() ile 2D koordinat ızgarası (grid) elde edilir. (X, Y) koordinatlari!
X, Y = np.meshgrid(x, y)

Z = np.sin(X) * np.cos(Y)

#plt.contour() → Sadece çizgileri çizer. Z'nin contour plotunu olusturduk!
#levels=20 → Kontur çizgilerinin sayısını (hassasiyeti) belirler.
#plt.contourf() → Alanları renkli doldurur.
plt.contour(X, Y, Z, levels=20, cmap="coolwarm") #Renk paletimiz de coolwarm oldu

#Add a colorbar to show the mapping between colors and function values.
plt.colorbar()
plt.title("Contour Plot")
plt.show()