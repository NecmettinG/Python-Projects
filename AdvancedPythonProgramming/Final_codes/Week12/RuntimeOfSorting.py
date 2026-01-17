import matplotlib.pyplot as plt
import numpy as np

#Bir algoritmanın giriş boyutu (𝑛) arttıkça çalışma süresinin (𝑇(𝑛)) nasıl değiştiğini gösterir.

n = np.linspace(500, 20000, 50)

a = 2.5e-6 # 2.5 * 10**(-6)

#Hata payı (gürültü) oluşturur.
#np.random.normal(mean, std, size):
#mean specifies the expected value (u) of the distribution,
#std specifies the standard deviation (o), which controls the spread,
#size specifies the number of random samples to generate.
E = np.random.normal(0, 0.002, size=len(n))

T = a * n * np.log2(n) + E

#Veriler noktalar halinde basılır.
plt.scatter(n, T)

plt.xlabel("Input Size N")
plt.ylabel("Runtime T(n) [s]")
plt.title("Algorithm runtime vs Input size")
plt.grid(True)
plt.show()