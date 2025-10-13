# Medical system processing patient data with critical accuracy requirements.
ID = "PAT2024-0892"
age = "45"
weight = "168.5"
height = "70"
blood = "120/80"
critical = "false"
extract_year = int(ID[3:7])

conv_age = int(age)
conv_weight = float(weight)
conv_height = float(height)
systolic, diastolic = map(int, blood.split("/"))
conv_critical = bool(critical)

BMI = conv_weight / conv_height
if systolic>=120 or diastolic>=80:
    print("blood pressure is high")
else:
    print("blood pressure is low")
risk_score = 0
risk_score += 1 if conv_age >= 60 else 0
risk_score += 1 if BMI >= 30 else 0
risk_score += 2 if conv_critical else 0

summary = (
    f"patient id : {ID}\n"
    f"age: {conv_age}\n"
    f"weight: {conv_weight}\n"
    f"height: {conv_height}\n"
    f"blood pressure: {systolic, diastolic}\n"
    f"critical: {conv_critical}\n"
    f"risk score: {risk_score}\n"
)
print(summary)