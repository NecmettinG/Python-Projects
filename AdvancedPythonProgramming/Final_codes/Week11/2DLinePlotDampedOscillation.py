import matplotlib.pyplot as plt
import numpy as np

#Generate t values between 0 and 20 using 500 points. (Time variable.)
t = np.linspace(0, 20, 500)

#Define the damped oscillatory function.
y = np.exp(-0.1*t) * np.sin(4*t)

#set the line width to 2 for better visibility. Plot the line.
plt.plot(t, y, linewidth=2, color="blue")

#Add labels and styling.
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("2D Line Plot of a Damped Oscillation")
plt.grid(True)

#Display the plot.
plt.show()