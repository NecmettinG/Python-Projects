s = input("Enter a string with at least three words: ")

if len(s.split()) >= 3:
    print("length: ", len(s),
          "\nlast character: ", s[-1],
          "\ntotal number of spaces: ", s.count(" "),
          "\nlowercase form: ", s.lower(),
          "\nuppercase form: ", s.upper(),
          "\nsplitted form: ", s.split(),
          "\ndashed form: ", "-".join(s.split()))