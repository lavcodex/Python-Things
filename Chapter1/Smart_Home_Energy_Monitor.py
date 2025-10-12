# A smart home system tracks appliance usage and converts between different data formats.
name = "Air Conditioner"
consumption = "1.5"
hours = "8.5"
rate = "0.12"
status = "on"

conv_consumption = float(consumption)
conv_hours = float(hours)
conv_rate = float(rate)

total = conv_consumption * conv_hours
cost = total * conv_rate
if status:
    print("Device Status is True")
else:
    print("Device Status is False")
result = round(cost,2)

print(f"Total cost: {result}")
print(f"Status tracking \ndevice name: {name}, consumption: {conv_consumption}, cost: {cost}, status: {status}")