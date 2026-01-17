x1 = int(input("Enter the x axis of p1: "))
y1 = int(input("Enter the y axis of p1: "))

x2 = int(input("Enter the x axis of p2: "))
y2 = int(input("Enter the y axis of p2: "))

distance = (((x1 - x2)**2) + ((y1 - y2)**2))**(1/2)

#biraz da string alistirmasi.
print("distance between two points is: ", distance,"\n---------\ndistance with scientific notation is: ", format(distance, ".3e"))