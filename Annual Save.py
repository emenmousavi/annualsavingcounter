print("""I am going to count your monthly and annual saving. Just please answer questions below.
How much is your Net Salary:""")
Salary = int(input())

print("Do you get any income out of your job? If yes, Please write it:")
Incm = int(input())

print("How much is your Rent:")
Rent = int(input())

print("How much is your Bills:")
Bills = int(input())

print("How much is your Shopping Expense:")
Shop = int(input())

print("How much is your Work Expense:")
Work = int(input())

print("How much is your Transportation Expense:")
Transp = int(input())

print("How much is your Entertainment Expense:")
Fun = int(input())

Spend = Fun + Transp + Work + Shop + Rent + Bills
Save = Salary + Incm
Left = Save - Spend
an_left = Left * 12

print(("So, Your Monthly Saving will be $" + str(Left)) + (" And your Annual Saving would be $" + str(an_left)))
