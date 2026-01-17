initialSpeed = float(input("Enter the initial speed of your car(m/s): "))
finalSpeed = float(input("Enter the final speed of your car(m/s): "))

distance = float(input("How much distance you progressed(meters): "))

acceleration = ((finalSpeed**2) - (initialSpeed**2)) / (2*distance)

print("acceleration is ", acceleration, " m/s^2\nacceleration with scientific notation is ", format(acceleration, ".3e"), " m/s^2")
