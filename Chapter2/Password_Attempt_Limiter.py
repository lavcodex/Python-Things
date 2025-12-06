# Allow user three attempts to enter correct password.

correct_password = "lavu123"
attempt = 1

while attempt <= 3:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Incorrect password")
        attempt += 1

if attempt > 3:
    print("Account Locked")
