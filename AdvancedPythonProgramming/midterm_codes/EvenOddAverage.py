evens = 0
odds = 0
total = 0
quantity = 0

number = int(input("Enter an integer, the input ends if it is 0: "))

while number != 0:

    quantity += 1
    total += number

    if number % 2 == 0:
        evens += 1

    else:
        odds += 1

    number = int(input("Enter an integer, the input ends if it is 0: "))

if quantity == 0:
    print("0 entered as the first number!")
else:
    print("The number of evens is: ", evens)
    print("The number of odds is: ", odds)
    print("The total is: ", total)
    print("The average is: ", float(total/quantity))