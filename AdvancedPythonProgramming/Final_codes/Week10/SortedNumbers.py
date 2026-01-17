def sortedNumbers(num1, num2, num3):

    ourList = [num1, num2, num3]

    ourList.sort()

    print("Numbers in increasing order: ", ourList[0], ourList[1], ourList[2])



number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

sortedNumbers(number1, number2, number3)