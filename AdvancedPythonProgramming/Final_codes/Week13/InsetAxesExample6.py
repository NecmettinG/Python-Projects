import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

x = np.linspace(0, 15, 200)

y = (x**2) * np.exp(-0.3 * x)

#fig → tüm pencere
#ax → ana eksen
fig, ax = plt.subplots(figsize=(7,5))

ax.plot(x, y, color="black")
ax.set_title("Zoom-in Inset Example")
ax.set_xlabel("x")
ax.set_ylabel("y = (x**2) * np.exp(-0.3 * x)")
plt.grid(True)

#Display the zoomed area in the lower right corner of the plot.
#ax → inset ana grafiğin içinde olacak
#width, height → ana grafiğin %35’i kadar
#loc="lower right" → sağ alt köşe
ax_inset = inset_axes(ax, width="35%", height="35%", loc="lower right")

#Zoom, aynı fonksiyonun detayını gösterecek
#Farklı veri çizilmiyor, sadece odak değişiyor
ax_inset.plot(x, y)

#Add a zoom-in inset that magnifies the region close to the peak of the curve, around x E [2,5].
#x = 2 ile 5 arasındaki noktalar seçiliyor
#mask → bu aralığı işaretleyen mantıksal dizi
x_min, x_max = 2, 5
mask = (x >= 2) & (x <= 5)

#Y sınırlarını otomatik belirleme
y_min, y_max = y[mask].min(), y[mask].max()

#Inset penceresi sadece 2–5 aralığını
#ve o aralıktaki y değerlerini gösterir
ax_inset.set_xlim(x_min, x_max)
ax_inset.set_ylim(y_min, y_max)

#Küçük pencerede yazı kalabalığı olmasın
#Sadece şekle odaklanılsın
ax_inset.set_xticks([])
ax_inset.set_yticks([])

plt.show()