print("""I am going to count your monthly and annual saving. Just please answer questions below.
How much is your Net Salary:""")
Salary = int(input())

print("Do you have a second job income as well? If yes, Please write the income below:")
Salary2 = int(input())

print("Do you get any income out of your job(s)? If yes, Please write the income below:")
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
Save = Salary + Incm + Salary2
Left = Save - Spend
an_left = Left * 12

print("Have you written your answers in Dollar?")

yesno = (input())

if yesno == "yes" or "Yes":
    print(("So, Your Monthly Saving will be $") + str(Left) + (" And your Annual Saving would be $") + str(an_left))
else:
    print("Please write your currency value to dollar:")
    currnc = int(input())
    conv_left = Left / currnc
    conv_annual = an_left / currnc
    print(("So, Your Monthly Saving will be $") + str(conv_left) + (" And your Annual Saving would be $") + str(conv_annual))
