# Monitor temperature and issue appropriate warnings.

temp = int(input("Enter temperature:"))

if temp > 90:
    print("heat warning")
if temp < 32:
    print("cold warning")
else:
    print("normal temperature")