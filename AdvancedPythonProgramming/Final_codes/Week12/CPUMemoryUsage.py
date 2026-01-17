import matplotlib.pyplot as plt
import numpy as np

#CPU ve Bellek gibi iki değişkenin eş zamanlı dağılımını (joint density) gösterir.
#En parlak bölgeler, sistemin en sık çalıştığı değer aralıklarını temsil eder.

#10000 samples for both of them.
cpu = np.random.normal(60, 15, 10000)
memory = np.random.normal(70, 10, 10000)

#Building 2D Histogram, 40 bins, "plasma" color map.
plt.hist2d(cpu, memory, bins=40, cmap="plasma")

plt.xlabel("Cpu usage %")
plt.ylabel("Memory usage %")

#Colorbar kullanılarak sağda yoğunluk seviyeleri gösteren bir referans çubuk beliriyor.
plt.colorbar(label="count")

plt.title("Cpu vs Memory usage joint density")
plt.show()