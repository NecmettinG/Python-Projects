import matplotlib.pyplot as plt
import numpy as np

#Şifre uzunluğu arttıkça kırma süresi üstel (2^c) arttığı için normal grafikler yetersiz.

c = np.arange(20, 61)

T = (2**c).astype(np.int32) / 1e6 #Hocanin pc 32 bit oldugundan astype(np.int32) kullandik.

plt.figure()

#plt.semilogy() → Y ekseni logaritmik yapılır.
#plt.semilogx() → X ekseni logaritmik yapılır.
plt.semilogx(c, T)

plt.xlabel("Key length in bits")
plt.ylabel("Time for cracking (s)")
plt.title("Password cracking time vs key length")

plt.grid(True, which="both")

plt.show()