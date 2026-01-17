import math

x1 = math.radians(float(input("Enter the latitude of A: ")))
y1 = math.radians(float(input("Enter the longitude of A: ")))

x2 = math.radians(float(input("Enter the latitude of B: ")))
y2 = math.radians(float(input("Enter the longitude of B: ")))

radius = 6371.01

greatCircleDistance = radius * math.acos(math.sin(x1)*math.sin(x2) + math.cos(x1)*math.cos(x2)*math.cos(y1-y2))

print(f"Great circle distance between A = ({math.degrees(x1)},{math.degrees(y1)}) and B = ({math.degrees(x2)}, {math.degrees(y2)}) is {round(greatCircleDistance, 3)} km.")