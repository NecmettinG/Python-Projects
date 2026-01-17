import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

#0 ile 10 arasında 500 eşit aralıklı nokta oluşturur
#Create 500 evenly spaced points between 0 and 10
x = np.linspace(0, 10, 500)

#Bu değerlerin sinüsünü hesaplar
#Compute the sine of these values
y = np.sin(x)

# Grafiği çizer
#Plot the resulting curve
plt.plot(x, y)

#Etiketler ve başlık ekler
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Basic 1D Line Plot")

#Görünüm ayarları
#Display the final plot
plt.grid(True)
plt.show()