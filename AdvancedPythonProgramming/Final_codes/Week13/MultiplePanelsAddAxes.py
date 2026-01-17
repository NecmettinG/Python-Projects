import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 200)

Y1 = np.sin(t)
Y2 = np.cos(t)

#Önce şu şekilde figure instance oluşturman lazım!!!
fig = plt.figure(figsize=(7,6))

#plt.subplots() otomatik bir ızgara yapısı oluştururken, fig.add_axes() metodu grafik panellerinin konumunu
# ve boyutunu tamamen manuel olarak belirlememize olanak tanır.

#Bu yöntemde kullanılan koordinatlar, tüm pencereye göre 0 ile 1 arasında normalize edilmiş oranlardır.

#ax = fig.add_axes([left, bottom, width, height])

ax1 = fig.add_axes([0.1, 0.2, 0.35, 0.7])

ax1.plot(t, Y1)
ax1.set_title("Sin(t)")

ax2 = fig.add_axes([0.55, 0.2, 0.35, 0.7])

ax2.plot(t, Y2, color="orange")
ax2.set_title("Cos(t)")

plt.show()