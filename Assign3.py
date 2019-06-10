import random
r = random.randint(1,20)
otp = ""
otp_count= 0
otp_limit = 3
out_of_otp = False
FirstName = raw_input("Enter First Name : ")
LastName = raw_input("Enter Last Name : ")
num = input("Enter the number : ")
if num > 20:
    print("Wrong input! try again")
for num in range(1,20):
    while otp != r and not (out_of_otp):
        if otp_count < otp_limit:
            otp = input("Enter otp : ")
            otp_count += 1
            if otp != r:
                print("Error!!! ENTER THE OTP AGAIN")
        else:
            out_of_otp = True
if out_of_otp:
    r = str(r)
    print("SORRY PROGRAM CRASHED " + r)
else:
    print("OTP SUCCESSFULLY MATCHED")





#for num in range(1,20):
#    if num > 20:
#        print("Wrong input! try again")
#    else:
#        x=input("continue ")
#        if x==No:
    #        print("Exit")
#        elif x==Yes:
#            num1 = input("Enter the number : ")
#            if num1 == r :
#                print("OTP SUCCESSFULLY MATCHED")
