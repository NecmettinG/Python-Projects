#This is an example of algorithm final exam!

total_cost = int(input("Enter the house's cost:"))

downpayment_percentage = int(input("Enter the percentage for downpayment:"))

current_savings = int(input("Enter your total current savings:"))

apr = (int(input("Enter the percentage of interest of deposited savings:")))/100

monthly_salary = int(input("Enter your monthly salary:"))

percentage_saved = int(input("Enter the percentage of saving salary:"))

salary_saved = (percentage_saved/100)*monthly_salary

percent_raise = int(input("Enter the precentage of your raising salary semi-annually:"))


inflation = (int(input("Enter the inflation:")))/100

loop = True

while True:

    for x in range(1,13):

        current_savings+=salary_saved
        current_savings = current_savings + (current_savings * apr/1200)

        if x == 6 or x == 12:

            monthly_salary +=monthly_salary * (percent_raise/100)

        if x == 12:

            total_cost+=total_cost*(inflation)

    message = input("Will you continue for 1 year again? (Y/N)")

    if message == "Y":

        continue

    elif message == "N":

        break

downpayment = (downpayment_percentage/100)*total_cost

total_month = downpayment/current_savings

print(f"The person have to save {total_month} month/months to pay downpayment.")
print("------------------------------------------------------------------------------------------------\end of the program")