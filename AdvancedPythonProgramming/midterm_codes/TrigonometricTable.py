import math

print(format("Degree", "<10s"), format("Sin", "<10s"), format("Cos", "<10s"), format("Tan", "<10s")) #s demek string demek.

for x in range(0, 361, 30):
    rad = math.radians(x)
    print(format(x, "<10d"), end="") #<10d demek x'i sola hizala ve 10 whitespace koy ve bunu decimal say

    sinVal = math.sin(rad)
    cosVal = math.cos(rad)

    if abs(cosVal) < 1e-12:
        tanVal = "Undefined"

    else:
        tanVal = format(math.tan(rad), "<10.4f")

    print(format(sinVal, "<10.4f"), end="") #<10.4f demek degeri sola hizala ve 10 whitespace yap ve noktadan sonraki 4 sayiya kadar roundla.
    print(format(cosVal, "<10.4f"), end="") #f demek float demek. Float say demek.
    print(tanVal)