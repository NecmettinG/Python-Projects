x1 = float(input("Enter x axis of big rectangle's center: "))
y1 = float(input("Enter y axis of big rectangle's center: "))

width1 = float(input("Enter the width of big rectangle: "))
height1 = float(input("Enter the height of big rectangle: "))

x2 = float(input("Enter x axis of small rectangle's center: "))
y2 = float(input("Enter y axis of small rectangle's center: "))

width2 = float(input("Enter the width of small rectangle: "))
height2 = float(input("Enter the height of small rectangle: "))

distanceX = abs(x1-x2)
distanceY = abs(y1-y2)

if distanceX <= (width1-width2)/2 and distanceY <= (height1-height2)/2:
    print("Small rectangle is inside of big rectangle.")
elif distanceX <= (width1+width2)/2 or distanceY <= (height1+height2)/2: #Bu condition and yerine or olmasi daha mantikli.
    print("Small rectangle overlaps with big rectangle.")
else:
    print("Small rectangle doesn't overlap with big rectangle.")