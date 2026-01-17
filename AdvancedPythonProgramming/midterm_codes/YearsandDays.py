minute = int(input("Enter a minute value: "))

days = minute // (24*60)

years = days//365

print(f"{minute} minutes are  {years} years and {days%365} days.")

