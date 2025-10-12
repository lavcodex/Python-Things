# Medical system processing patient data with critical accuracy requirements.
ID = "PAT2024-0892"
age = "45"
weight = "168.5"
height = "70"
blood = "120/80"
critical = "false"
extract_year = 2024

conv_age = int(age)
conv_weight = float(weight)
conv_height = float(height)
conv_critical = bool(critical)

BMI = conv_weight / conv_height
if blood:
    print("blood pressure is high")
else:
    print("blood pressure is low")
