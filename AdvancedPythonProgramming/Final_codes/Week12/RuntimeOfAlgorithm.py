import matplotlib.pyplot as plt
import numpy as np

#n is in between [10**3, 10**6] with 200 logarithmically spaced points! (You won't use linspace this time!)
#Giriş boyutunu 1.000 – 1.000.000 arasında logaritmik artırır.
n = np.logspace(3, 6, 200) #Soruda logarithmically spaced points diyor! Sakın linspace kullanma!!! logspace olacak!
#Ayrıca soruda 10**3 ve 10**6 diyor, logspacein içine sadece 10'ların üstündeki sayıları gir!

a = 2e-7
b = 5e-6

T = a * n * np.log2(n) + b * n

#Hoca color olarak "red" ve marker olarak "o" tercih etmiş! Ama soruda da belirtmemiş :D.
#Büyük veri setlerinde performans değişimi doğrusal olmayan eksende gösterilir.
plt.plot(n, T, color="red", marker="o")

plt.title("Runtime of Algorithm (Line Plot)")
plt.xlabel("Input size n")
plt.ylabel("Runtime T(n) [s]")

plt.grid(True)

plt.show()