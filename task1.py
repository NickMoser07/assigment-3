principle = int(input("please enter your principle"))
monthlyIrate = int(input("what is your yearly interest rate"))
numOfmonths = int(input("how many months"))
paymentAmount = int(input("how much do you want to add each month"))
monthlyIrate /= 100
monthlyIrate /= 12

futureValue = (principle * ( 1 + monthlyIrate) ** numOfmonths) + paymentAmount * ((((1+monthlyIrate)**numOfmonths)-1)/monthlyIrate) * (1+monthlyIrate)    
print(futureValue)