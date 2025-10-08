#Track whether a user is logged into an online store.
name=input("Enter a username:")
status_input=input("Enter a login status(True/False):").lower()
status = True if status_input == "True" else False
print(f"online store login \nThe username is {name}, and login status is {status} ")