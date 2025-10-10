# Convert various fitness metrics from string inputs to appropriate types.
steps_str = "10500"
distance_str = "5.2"
activity = "active"

conv_steps = int(steps_str)
conv_distance = float(distance_str)
conv_activity = activity.lower() == "active"

summary = f"Steps: {conv_steps}, Distance: {conv_distance}, Activity: {conv_activity}"
print(summary)