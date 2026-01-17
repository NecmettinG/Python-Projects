while True:
    airlineNumber = int(input("Enter the number of airlines: "))
    if airlineNumber >= 1:
        break

cheapestTicket = None #Initialization icin buraya koydum.
cheapestName = None #Initialization icin buraya koydum.
for x in range(1, airlineNumber+1):

    airlineName = input("Enter an airline name: ")
    ticket = int(input("Enter ticket price: "))

    if x == 1:
        cheapestTicket = ticket
        cheapestName = airlineName
        continue

    if ticket < cheapestTicket:
        cheapestTicket = ticket
        cheapestName = airlineName

print(f"Cheapest airline {cheapestName}'s ticket price is {cheapestTicket:.2f}")

#Hoca biraz daha farkli cozmus ama mantik ve outputlar ayni.