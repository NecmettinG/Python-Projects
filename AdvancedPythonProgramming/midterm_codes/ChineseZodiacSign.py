year = eval(input("Enter the year: ")) #int(input("Enter the year: ")) yerine eval kullandik. Eval icindeki kod execute ediliyor.

zodiacSign = year % 12

if zodiacSign == 0:
    print("monkey")
elif zodiacSign == 1:
    print("rooster")
elif zodiacSign == 2:
    print("dog")
elif zodiacSign == 3:
    print("pig")
elif zodiacSign == 4:
    print("rat")
elif zodiacSign == 5:
    print("ox")
elif zodiacSign == 6:
    print("tiger")
elif zodiacSign == 7:
    print("rabbit")
elif zodiacSign == 8:
    print("dragon")
elif zodiacSign == 9:
    print("snake")
elif zodiacSign == 10:
    print("horse")
else:
    print("sheep")