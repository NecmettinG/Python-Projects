import math

radius = float(input("Enter the radius of the circle: "))

if radius >= 0:
    area = (radius**2) * math.pi #Pi sayisini math kutuphanesiyle kullanabiliyoz.
    print("Area of the circle is: ", format(area, ".4f"))

else:
    print("Radius cannot be negative!")