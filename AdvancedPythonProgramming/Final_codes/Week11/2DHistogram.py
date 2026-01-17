import matplotlib.pyplot as plt
import numpy as np

#Veri düzlemi küçük karelere (bin) bölünür.
#Her kareye düşen veri noktası sayısı hesaplanır.
#Yoğun bölgeler daha parlak/yoğun renklerle gösterilir.

#Generate 10,000 random values for variable c from a standard normal distribution.
x = np.random.randn(10000)

#Generate 10,000 random values for variable y, where y = 0.5*E + 2
#and E ~ N(0, 1), so that the distribution of y is shifted and scaled.
y = np.random.randn(10000) * 0.5 + 2

#40 bölmeli (bin), plasma renk temasına sahip 2D histogram oluşturur.
plt.hist2d(x, y, bins=40, cmap="plasma")

#Yoğunluk ölçeğini grafiğin yan tarafına colorbar olarak ekler. ("Count" olarak labellanacak)
plt.colorbar(label="Count")

plt.xlabel("x")
plt.ylabel("y")
plt.title("2D Histogram")
plt.show()