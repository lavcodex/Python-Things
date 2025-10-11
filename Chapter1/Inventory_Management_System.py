# A warehouse system needs to process mixed data types from barcode scanners and manual entries.
id = "PRD-12345"
current = "245"
minimum = "100"
price = "15.99"
available = "yes"
Extract_p_id = 12345

conv_current = int(current)
conv_minimum = int(minimum)
conv_price = float(price)
conv_available = bool(available)

reorder = conv_current < conv_minimum
stock = conv_current * conv_price
print(f"Inventory Tracking Status Report\nProduct ID: {id}\nCurrent stock: {conv_current}\nMinimum stock: {conv_minimum}\nUnit price: {conv_price}\nProduct available: {conv_available}\nReorder: {reorder}\nStock value: {stock}")