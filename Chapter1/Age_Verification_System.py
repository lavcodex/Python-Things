# A website needs to verify if users meet the minimum age requirement.

current_year = 2024
birth_y_str = "1998"
conv_birth_y = int(birth_y_str)

age = current_year - conv_birth_y
print(f"Age: {age} ")

if age >= 21:
    print("Eligibility to True")
else:
    print("False")
