number = int(input("Enter a number: "))

print("Is", number, "divisible by 2 and 3? ", number % 2 == 0 and number % 3 == 0)

print("Is", number, "divisible by 2 or 3? ", number % 2 == 0 or number % 3 == 0)

print("Is", number, "divisible by 2 or 3 but not both? ", (number % 2 == 0 or number % 3 == 0) and not (number % 2 == 0 and number % 3 == 0))

