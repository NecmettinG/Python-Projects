import random

char1 = chr(random.randint(ord('A'),ord('Z')))
char2 = chr(random.randint(ord('A'),ord('Z')))
char3 = chr(random.randint(ord('A'),ord('Z')))

char4 = chr(random.randint(ord('0'),ord('9')))
char5 = chr(random.randint(ord('0'),ord('9')))
char6 = chr(random.randint(ord('0'),ord('9')))
char7 = chr(random.randint(ord('0'),ord('9')))

print("Generated plate is: ", char1+char2+char3+char4+char5+char6+char7)