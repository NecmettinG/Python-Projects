import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)

F1 = np.sin(x)
F2 = np.cos(x)
F3 = np.exp(-0.2 * x)
F4 = 0.1 * x**2
F5 = np.log(x+1)

plt.figure(figsize=(10,5))

plt.plot(x, F1, label="sin(x)", color="red")
plt.plot(x, F2, label="cos(x)", color="blue")
plt.plot(x, F3, label="exp(-0.2 * x)", color="green")
plt.plot(x, F4, label="0.1 * x**2", color="pink")
plt.plot(x, F5, label="ln(x+1)", color="orange")

plt.xlabel("x")
plt.ylabel("Different function values")
plt.title("Different functions on the same axes.")

plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()