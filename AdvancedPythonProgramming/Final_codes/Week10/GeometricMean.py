def geo_mean(*args):

    count = 0
    product = 1

    #Eger fonksiyona hic deger yollamazsak bu loopa girmeyecez.
    for i in args:

        if not isinstance(i, (int, float)):
            return "Error: Geometric mean can only be computed with numeric values."

        count += 1
        product *= i

    if count == 0:

        return "At least one numeric value is required."

    return product**(1/count)


print(geo_mean(2, 4, 8))
print(geo_mean(10, "x", 2))
print(geo_mean())