# Count total steps for a week.

total_steps = 0
day = 1

while day <= 7:
    steps = int(input("enter steps of day{day}:"))
    total_steps += steps
    day += 1
    
print("total steps for the week : ",total_steps)