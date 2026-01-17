weight = float(input("Enter your weight in kilograms unit: "))
height = float(input("Enter your height in meters unit: "))

BMI = weight / height**2

print("your body mass index is: ", format(BMI, ".3f"))