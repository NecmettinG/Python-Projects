import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 1000)

mse = (x**2 - x)**2
mae = np.abs(x**2 - x)

#For part A: plotting mse(Mean Squared Error) and mae(Mean absolute error) on the same axes:

fig, ax = plt.subplots(figsize=(8,7))

ax.plot(x, mse, label="MSE", color="red", linewidth=3)
ax.plot(x, mae, label="MAE", color="blue", linewidth=3)
ax.set_title("MAE vs MSE on same plot")
ax.legend()

fig2, axes = plt.subplots(1, 2, figsize=(8,7))

axes[0].plot(x, mse, label="MSE", color="red", linewidth=2)
axes[0].set_title("MSE subplot")
axes[1].plot(x, mae, label="MAE", color="blue", linewidth=2)
axes[1].set_title("MAE subplot")

plt.show()


