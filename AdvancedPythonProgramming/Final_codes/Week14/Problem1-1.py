import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 1000)

A1 = 1
A2 = 0.6
f1 = 5
f2 = 8

x1 = A1 * np.sin(2 * np.pi * f1 * t)
x2 = A2 * np.sin(2 * np.pi * f2 * t)

#overlapping plot:
plt.figure(figsize=(8,6))

plt.plot(t, x1, color="red", label="x1")
plt.plot(t, x2, color="blue", label="x2")

plt.title("Overlapping plot of x1 and x2")
plt.xlabel("t")
plt.ylabel("x")

plt.grid(True)
plt.legend()
plt.show()
