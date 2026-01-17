import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2, 2000)

displacement = 0.05 * np.exp(-0.08 * 25 * t) * np.sin(25 * np.sqrt(1 - 0.08**2) * t)

#Bunu boşu boşuna koymuş gibi. plt.figure(figsize=(10,5), dpi=150) gibi kullansa neyse de, commente bile alabilirsin bunu. O kadar boş.
plt.figure()

plt.plot(t, displacement, color="green")

plt.xlabel("t (s)")
plt.ylabel("x(t) (m)")
plt.title("Damped Free Vibration: x(t)")

plt.grid(True)
plt.show()
