#Calculate membership discount based on duration and age.

base_price = float(input("Enter base membership price: "))
duration = int(input("Enter membership duration in months: "))
age = int(input("Enter member age: "))

discount = 0

if duration >= 12:
    discount += 20
elif duration >= 6:
    discount += 10

if age < 25 or age >= 65:
    discount += 5

final_price = base_price - (base_price * discount / 100)

print("\n----- Membership Discount Summary -----")
print("Base Price: ₹", base_price)
print("Total Discount Applied:", discount, "%")
print("Final Price to Pay: ₹", final_price)
