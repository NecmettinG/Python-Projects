def process(value):

    if value > 0:

        return (lambda x : x * 2)(value)

    elif value < 0:

        return (lambda x : abs(x) + 5)(value)

    else:
        return (lambda x : 0)(value)


print(process(10))
print(process(-4))
print(process(0))