otp = 1234
guess = ""
otp_count = 0
otp_limit = 3
out_of_otp = False
while guess != otp and not(out_of_otp):
    if otp_count < otp_limit:
        guess = input("Enter guess: ")
        otp_count += 1
    else:
        out_of_otp = True
if out_of_otp:
    print("SORRY TRY AGAIN")
else:
    print("SUCCESSFULL")

def menu():
    money = int(5000)
    #print the options you have
    print "Welcome to the Python Bank System"
    print " "
    print "Your Transaction Options Are:"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "1) New Account"
    print "2) Deposit"
    print "3) Withdraw"
    print "4) Balance Inquiry"
    print "5) Demand Draft"
    print "6) Cancel"
    return input ("Choose your option: ")

def new_account(balance, money):
    Name = raw_input("Enter Name : ")
    Age = raw_input("Enter Age : ")
    Address = raw_input("Enter Address : ")
    Contact = raw_input("Enter Contact : ")
    Gender = raw_input("Enter Gender : ")
    print ("ACCOUNT HOLDER DETAILS")
    return
#Here is the deposit part.... This is where the user inputs the amount of money
#they wish to deposit into their account.
def deposit(money):
    global balance
    deposit = float(input("Enter amount to be Deposited : $"))
    if deposit <= money:
        balance += deposit
        print "You've successfully deposited $", deposit, "into your account."
        bank_balance(balance)
        return balance
#This is where the user inputs the amount of money they wish to withdraw from
#their account. Currently not programmed in as of yet.
def withdrawl(balance, money):
    withdraw = float(input("Enter amount to be withdrawl : $"))
    if balance >= withdraw:
        balance -= withdraw
        print "HERE IS YOUR MONEY $",withdraw
    else:
        print("Insufficient balance")
        bank_balance(balance)
        return balance
#This is an obvious one, this is where you check your balance.
def bank_balance(balance):
    print "Balance: $", balance
    return balance
# NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
balance = 0
money = 5000
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        account = new_account(balance, money)
    elif choice == 2:
        deposit = deposit(money)
    elif choice == 3:
        withdraw = withdrawl(balance, money)
    elif choice == 4:
        balance = bank_balance(balance)
    elif choice == 5:
        loop = 0
print "Thank-You for stopping by the bank!"
#END OF THE PROGRAM
