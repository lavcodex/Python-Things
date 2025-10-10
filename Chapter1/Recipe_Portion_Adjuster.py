# A cooking app needs to adjust recipe quantities based on serving size.
original = 4
desired_str = "6"
ingredient = 2.5
conv_desired = int(desired_str)

scaling_factor = conv_desired / original
result = ingredient * scaling_factor
conv_result = str(result)
print(f"serving size: {conv_result} cups")