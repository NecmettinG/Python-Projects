number = int(input("Enter a positive integer: "))

print(f'The prime numbers for {number} is', end=" ")

factor = 2

while factor<=number:

    if number%factor == 0:
        number //= factor
        print(factor, end=" ")

    else:
        factor += 1
