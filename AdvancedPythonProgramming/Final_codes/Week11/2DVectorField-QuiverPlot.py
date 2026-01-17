import matplotlib.pyplot as plt
import numpy as np

#create two 20x20 coordinate grids X and Y spanning the region from —3 to 3 in both directions.
Y, X = np.mgrid[-3:3:20j, -3:3:20j]

#Define the vector components.
U = -Y
V = X

#Merkezin etrafında dönen bir dönel akış (rotational flow) oluşturduk.
#plt.quiver(X, Y, U, V) → Vektörleri koordinat düzlemine oklar şeklinde yerleştirir.
plt.quiver(X, Y, U, V)

plt.title("2D Vector Field")
plt.show()