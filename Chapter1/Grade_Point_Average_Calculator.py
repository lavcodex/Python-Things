# Convert letter grades to numerical values for GPA calculation
grade_str = "B+"
hours_str = "3"
value = "3.3"
conv_value = float( value)
print(f"{grade_str} = {conv_value}")
conv_hours = int(hours_str)

grade_point = conv_value * conv_hours
print(f"grade point: {grade_point}")

if conv_value >= 2.0:
    print("True ")
else: 
    print("False")

