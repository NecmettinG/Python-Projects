import matplotlib.pyplot as plt
import numpy as np

#Generate 200 random values for the variable x, uniformly distributed in the interval [0, 1].
x = np.random.rand(200)

#Create a dependent variable y = 2x + 0.3E (E is standart normally distributed noise.).
y = 2*x + 0.3*np.random.randn(200)

#Produce a 2D scatter plot of the generated points (x, y).
plt.scatter(x, y, alpha=0.6) #setting the point transparency(saydamlık) to 0.6 (alpha)
plt.xlabel("x")
plt.ylabel("y")
plt.title("2D Scatter Plot")

plt.grid(True) #enabling grid lines.
plt.show() #display the final plot.
