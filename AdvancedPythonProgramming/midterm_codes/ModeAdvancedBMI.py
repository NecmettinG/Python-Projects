weight = eval(input("Enter your weight(kg): "))
height = eval(input("Enter your height(meters): "))

BMI = weight/height**2

print("Your body mass index is ", format(BMI, ".2f"))

if BMI < 18.5:
    print("You are underweight.")
    print("Risk of developing heart problems is increased.")
elif BMI < 25:
    print("Your weight is normal")
    print("Risk of developing heart problems is least.")
elif BMI < 30:
    print("You are overweight")
    print("Risk of developing heart problems is increased.")
elif BMI < 35:
    print("You are obese class 1")
    print("Risk of developing heart problems is high.")
elif BMI < 40:
    print("You are obese class 2")
    print("Risk of developing heart problems is very high.")
else:
    print("You are obese class 3")
    print("Risk of developing heart problems is extremely high.")