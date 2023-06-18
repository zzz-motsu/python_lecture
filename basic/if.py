age = 17
age_alcohol = 20

if age >= age_alcohol:
    print("You can drink beer!")
else:
    print("You are too young to drink beer!")

age_drive = 18
if age >= age_alcohol:
    print("You can drink beer!")
elif age < age_drive:
    print("You cannot even drive!")
else:
    print("You are not allowed to drink beer but you can drive only if you have driver's licence")

if not 0 < age < 120:
    print("The value is invalid!!")

balance = 1000
withdrawal = 600
withdrawal_limit = 500

if withdrawal > withdrawal_limit:
    print(f"The withdrawal limit is {balance}")
elif balance >= withdrawal:
    # balance = balance - withdrawal
    balance -= withdrawal
    # print("You new balance is {}".format(balance))
    print(f"You new balance is {balance}")
else:
    print("You don't have money")
