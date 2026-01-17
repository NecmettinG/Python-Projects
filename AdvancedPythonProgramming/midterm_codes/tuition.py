current = 10000
totalCost = 0

for i in range(1, 11):
    #current += current*(5/100)
    current *= 1.05

print(f"Tuition in 10 years is: {current:.4f}")

for x in range(1,5):
    current += current * (5 / 100) #73717.7643
    #current *= 1.05 #73717.7643
    totalCost += current

print("The four year total tuition in 10 years is: ", round(totalCost, 4))