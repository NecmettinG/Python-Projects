n = 0

while n<2:
    n = int(input("Enter an integer n>=2: "))

factor = 2

while factor<=n:

    if n%factor == 0:
        break
    factor += 1
print("Smallest factor other than 1 for ", n, " is ", factor, ".")