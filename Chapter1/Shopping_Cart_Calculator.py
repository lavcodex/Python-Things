# An online store needs to convert string prices from user input to calculate totals.
price_str = "19.99"
quantity_str = "3"

conv_price = float(price_str)
conv_quantity = int(quantity_str)

mul = conv_price * conv_quantity
prefix = "$" + str(round(mul,2))

print("Total cost :",prefix)