import sys

twoCharacters = input("Enter your major and status: ")

if len(twoCharacters) == 2:
    if twoCharacters[0] == "M":
        print("Mathematics")
    elif twoCharacters[0] == "C":
        print("Computer Science")
    elif twoCharacters[0] == "I":
        print("Information Technology")
    else:
        print("invalid major!")
        sys.exit("Invalid Major")

    if twoCharacters[1] == "1":
        print("Freshman")
    elif twoCharacters[1] == "2":
        print("Sophomore")
    elif twoCharacters[1] == "3":
        print("Junior")
    elif twoCharacters[1] == "4":
        print("Senior")
    else:
        print("invalid status!")