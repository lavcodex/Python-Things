#An ATM needs to check if a withdrawal amount is valid

amount =int (input("enter a amout:"))
balance = int (input("enter a balance:"))

if amount>0:
    print("withdrawal amount is greater than 0")
else:
    if amount%20!=0:
        print("withdrawal amount must be multiply by 20")
    else:
        if amount<=0:
            print("withdrawal Approved")
        else:
            print("Insufficient balance")
