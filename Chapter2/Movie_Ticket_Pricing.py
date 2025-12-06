# A cinema charges different prices based on age.

age = int(input("Enter age:"))
if age < 12:
    price = 5
elif age >= 65:
    price = 8
else:
    price = 12
print("Ticket Price: $",price)