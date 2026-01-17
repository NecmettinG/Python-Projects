def apply_lambda(*args):

    f = lambda x : x**2 + 1

    outputList = list(map(f, args))

    return outputList

    #return [f(x) for x in args] (list comprehension)
    # [f(x) for x in args] yapısı, gelen tüm sayıları tek tek bu kuraldan geçirip yeni bir liste oluşturur.

print(apply_lambda(1,2,3))
print(apply_lambda(1,2,3,4,5))