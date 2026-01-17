def transform(variable):

    if isinstance(variable, list):
         return variable[::-1]

    elif isinstance(variable, str):
        return variable.upper()

    elif isinstance(variable, int):

        sum = 0

        while variable > 0:

            digit = variable % 10

            sum += digit

            variable = variable // 10

        if sum == 0:
            return "Your integer is negative or 0. You must enter a positive integer."

        return sum

    else:
        return "Unsupported Type!"

print(transform([1,2,3]))
print(transform("elif"))
print(transform(246))
print(transform(3.14))
print(transform(-5))