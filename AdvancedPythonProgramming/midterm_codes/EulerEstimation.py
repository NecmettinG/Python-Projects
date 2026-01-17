e = 1

denominator = 1

for x in range(1, 21):

    denominator *= x
    e += 1/denominator
    print(f"for n = {x}, e = {e}")
