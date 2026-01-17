import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

#Sin(x) fonksiyonunun, x değeri 1 ile 2 arasındaki bölümünü büyütülmüş bir pencere içerisinde göstermemizi istiyor.

x = np.linspace(0,10, 200)

y = np.sin(x)

fig, ax = plt.subplots(figsize=(7,5))

ax.plot(x, y, color="black")

ax.set_title("Sin(x) with inset axes")
ax.set_xlabel("x")
ax.set_ylabel("Sin(x)")
ax.grid(True)

#inset_axes fonksiyonu ile ana eksenin içine küçük bir panel tanımlamalıyız.
#Create inset axes
ax_inset = inset_axes(ax, width="35%", height="35%", loc="upper right")

#plot inside inset
ax_inset.plot(x, y)

#Add a zoom-in inset focusing on the interval x E [1,2]
#define zoom region
x_min, x_max = 1, 2

#Y'leri de böyle belirliyon!!!
mask = (x >= x_min) & (x <= x_max)
y_min, y_max = y[mask].min(), y[mask].max()

#Setting the zoom region
#ax_inset.set_xlim(1, 2) komutu ile yakınlaştırılacak bölgeyi belirlemeliyiz.
ax_inset.set_xlim(x_min, x_max)
ax_inset.set_ylim(y_min, y_max)

ax_inset.set_xticks([])
ax_inset.set_yticks([])

plt.show()