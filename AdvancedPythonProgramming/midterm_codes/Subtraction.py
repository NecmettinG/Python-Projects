import random

number1 = random.randint(0,9)
number2 = random.randint(0,9)

if number1 < number2:
    number1, number2 = number2, number1

answer = int(input(f"what is the answer of {number1} - {number2} ? "))

if answer == (number1 - number2):

    print("You are correct!")

else:
    print("Your answer is wrong.\n", number1, " - ", number2, " is ", number1-number2)

