import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 40)

temperature = 25 + (120 - 25) * np.exp(-1.6 * x)

plt.figure()

#40 ölçüm noktası plt.scatter ile tek tek işaretlenir.
plt.scatter(x, temperature)

plt.title("Temperature Along the Plate")
plt.xlabel("x [m]")
plt.ylabel("Temperature T(x) Celcius (Scatter)")

plt.grid(True)
plt.show()