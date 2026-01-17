import math

x1 = float(input("Enter the x axis for point 1: "))
y1 = float(input("Enter the y axis for point 1: "))

x2 = float(input("Enter the x axis for point 2: "))
y2 = float(input("Enter the y axis for point 2: "))

x3 = float(input("Enter the x axis for point 3: "))
y3 = float(input("Enter the y axis for point 3: "))


a = math.sqrt((x2-x3)**2 + (y2-y3)**2)
b = math.sqrt((x1-x3)**2 + (y1-y3)**2)
c = math.sqrt((x1-x2)**2 + (y1-y2)**2)

A = math.degrees(math.acos((a**2 - b**2 - c**2)/(-2*b*c)))
B = math.degrees(math.acos((b**2 - a**2 - c**2)/(-2*a*c)))
C = math.degrees(math.acos((c**2 - b**2 - a**2)/(-2*a*b)))

print("The angle of A is ", round(A, 3),"in degrees.")
print("The angle of B is ", round(B, 3),"in degrees.")
print("The angle of C is ", round(C, 3),"in degrees.")