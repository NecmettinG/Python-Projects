import math

x = int(input("Enter x axis: "))
y = int(input("Enter y axis: "))

radius = int(input("Enter the radius of the circle: "))

distance = math.sqrt((x**2)+(y**2))

if distance <= radius:
    print(f"point ({x}, {y}) is in circle.")
else:
    print(f"point ({x}, {y}) is outside of circle.")