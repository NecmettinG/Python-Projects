import matplotlib.pyplot as plt
import numpy as np

#Zaman içindeki sinüzoidal (dalgalı) değişimi gösterir.
#Ağ gecikmelerindeki periyodik artış ve azalışları modellemek için kullanılır.

t = np.linspace(0, 50, 500)

noise = np.random.normal(0, 1, size=len(t))

#20 + 5*np.sin(0.4*t) → Temel dalga formu.
delay = 20 + 5 * np.sin(0.4 * t) + noise

#plt.plot(t, delay) → Noktalar çizgi ile bağlanarak akış gösterilir.
plt.plot(t, delay, color="orange")

plt.xlabel("time t [s]")
plt.ylabel("packet delay d(t) [ms]")
plt.title("Network Packet Delay 2D Line Plot")

plt.grid(True)
plt.show()