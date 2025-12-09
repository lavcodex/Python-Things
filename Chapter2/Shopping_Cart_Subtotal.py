# Calculate subtotal of items in shopping cart.

cart = [120.50,80.00,45.00,200.00]
subtotal = 0
for price in cart:
    subtotal += price
print("shopping cart subtotal: $",subtotal)