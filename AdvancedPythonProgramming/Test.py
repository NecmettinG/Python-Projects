print("sen anani\b yani.")

print("a b c d".rsplit(' ', 1))

print("AL".center(8, '*'))
print("AL".ljust(8, '*'))

print(ord('A'))

x = 1234567.89101112131415
print(format(x, ".11e"))

x = 0.000012346
print(f"{x:.3e}")

print(round(6.5))
print(round(6192.347384, 4))
print(format(6192.347384, ".4f"))
print(format(6192.347384, ".4e"))

print("Hello {}. {} to meet you.".format("world", "Nice"))

print("EXPECTATIONS", end=" ")
print("GO", end=" ")
print("TO HELL", end="!\n")

print("banana".replace("a", "i"))

print("A~B~C~D".rsplit("~", 1))
print("A~B~C~D".rsplit("~", 2))

print(len("Hallo Evernyan Hawa u".split()))
print("Hallo Evernyan Hawa u".count(" "))

number = str(123456)
print(number.split("3"))

myList = [1,2,3]
myList.reverse()
print(myList)