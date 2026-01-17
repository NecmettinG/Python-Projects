def findEvenAndOdd(number):

    evenCount = 0
    oddCount = 0



    if number > 0:

        numberString = str(number)

        for i in numberString:

            if int(i) % 2 == 0:
                evenCount += 1

            else:
                oddCount += 1

        return evenCount, oddCount

    else:

        return evenCount, oddCount


number = int(input("Enter a positive integer: "))

even, odd = findEvenAndOdd(number)

print("Even digits: ", even)
print("Odd digits: ", odd)