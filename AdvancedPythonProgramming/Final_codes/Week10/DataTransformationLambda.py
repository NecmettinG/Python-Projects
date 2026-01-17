def process(variable):

    if isinstance(variable, list):
        f = lambda x : x[::-1]

    elif isinstance(variable, str):
        f = lambda x : x.upper()

    elif isinstance(variable, int):
        f = lambda x : len(str(x))

    else:
        return "unsupported type!"

    return f(variable)

print(process([1,2,3]))
print(process("hello"))
print(process(246))
print(process(3.14))
