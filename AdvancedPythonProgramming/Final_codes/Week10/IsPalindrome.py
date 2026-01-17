def reverse(number):

    return int(str(number)[::-1])

def isPalindrome(number):

    return number == reverse(number)

globalNumber = int(input("Enter a number for checking if it is a palindrome or not: "))

condition = isPalindrome(globalNumber)

if condition:
    print(globalNumber, " is palindrome.")

else:
    print(globalNumber, " is not palindrome.")

