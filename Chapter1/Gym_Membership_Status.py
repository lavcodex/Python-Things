#A gym tracks whether memberships are active.
id=int(input("Enter a member ID:"))
active_status=bool(input("Enter a active status (True/False):"))
status=True if active_status == True else False
print(f"Gym Membership Status \nThe gym member ID is {id} and it's {active_status} membership is active")