sum1 = 0
number = 0
while number < 20:
    number += 1
    if number == 10 or number == 11:
        continue
    sum1 += number
numbers = range(1, 21) #RANGE I UNUTMA CUNKU YENİ BU LIST GIBI
print(type(numbers))
sum2 = sum(numbers)
print('The sum except 10 and 11 is', sum1)
print('The sum 1 to 20 by sum built-in function is', sum2)
