import math

print(format("Real Number", "<15s"), format("Cube Root", "<15s"))

for number in range(0, 51, 4):

    cubeRoot = math.pow(number, 1/3) # veya sadece pow(number, 1/3).


    print(format(number, "<15d"), end="")
    print(format(cubeRoot, "<15.4f"))