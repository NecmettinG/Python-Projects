annualInterestRate = float(input("Enter the annual interest rate (in percentage):"))

monthlyInterestRate = annualInterestRate / (100*12) #Bu kısmı biraz daha ezberle her gun nisaya hatırlat fksdnfkjs

loanAmount = float(input("Enter the loan you took:"))

years = int(input("How many years? "))

monthlyPayment = (loanAmount * monthlyInterestRate) / (1 - (1 / (1 + monthlyInterestRate)**(years * 12)))

totalPayment = monthlyPayment * years * 12

print("The monthly payment is ", format(monthlyPayment, ".4f")) #format(monthlyPayment,".5e")) yerine bunu kullanim dedim.
print("The total payment is ", format(totalPayment, ".4f"))

print("----------------------")

print("The monthly payment is ", format(monthlyPayment, ".5e"))
print("The total payment is ", format(totalPayment, ".5e"))