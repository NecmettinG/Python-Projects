import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 1000)

A1 = 1
A2 = 0.6

f1 = 5
f2 = 8

x1 = A1 * np.sin(2 * np.pi * f1 * t)
x2 = A2 * np.sin(2 * np.pi * f2 * t)

fig, axes = plt.subplots(2, 1, figsize=(8,6))

axes[0].plot(t, x1, color="red")
axes[0].set_title("x1 graph")
axes[0].set_ylabel("x1")
axes[0].grid(True)

axes[1].plot(t, x2, color="blue")
axes[1].set_title("x2 graph")
axes[1].set_ylabel("x2")
axes[1].grid(True)

plt.tight_layout()
plt.show()