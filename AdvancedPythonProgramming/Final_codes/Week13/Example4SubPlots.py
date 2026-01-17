import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10, 400)

F1 = np.sin(x)
F2 = np.cos(x)
F3 = np.exp(-0.2*x)
F4 = 0.1 * x**2
F5 = np.log(x + 1)

fig, axes = plt.subplots(5, 1, figsize=(9,12))

axes[0].plot(x, F1, color="blue")
axes[0].set_title("Sin(x)")
axes[0].set_xlabel("x")
axes[0].set_ylabel("Sin(x)")
axes[0].grid(True)

axes[1].plot(x, F2, color="red")
axes[1].set_title("Cos(x)")
axes[1].set_xlabel("x")
axes[1].set_ylabel("Cos(x)")
axes[1].grid(True)


axes[2].plot(x, F3, color="green")
axes[2].set_title("exp(-0.2*x)")
axes[2].set_xlabel("x")
axes[2].set_ylabel("exp(-0.2*x)")
axes[2].grid(True)


axes[3].plot(x, F4, color="orange")
axes[3].set_title("0.1 * x**2")
axes[3].set_xlabel("x")
axes[3].set_ylabel("0.1 * x**2")
axes[3].grid(True)


axes[4].plot(x, F5, color="black")
axes[4].set_title("ln(x+1)")
axes[4].set_xlabel("x")
axes[4].set_ylabel("ln(x+1)")
axes[4].grid(True)



plt.tight_layout()
plt.show()