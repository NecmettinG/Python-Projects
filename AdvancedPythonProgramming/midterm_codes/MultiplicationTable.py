print("Multiplication Table")
print("    ", end="")

for x in range(1,10):
    print(f"{x:4d}", end="") #:4d 4 tane whitespace birakiyor bilgin olsun.

print("\n---------------------------------")

for i in range(1,10):
    print(i, "| ", end="")
    for j in range(1,10):
        print(f"{i*j:4d}", end="")
    print("\n")