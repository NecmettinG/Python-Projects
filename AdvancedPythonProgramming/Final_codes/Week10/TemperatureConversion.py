def celciusToFahrenheit(celcius):

    F = ((9/5) * celcius) + 32

    return F


def fahrenheitToCelcius(fahrenheit):

    C = (5 / 9) * (fahrenheit - 32)

    return C


celcius = float(input("Enter temperature in Celcius: "))

print("In Fahrenheit: ", celciusToFahrenheit(celcius))

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

print("In Celcius: ", fahrenheitToCelcius(fahrenheit))