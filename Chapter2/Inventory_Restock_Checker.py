# Check each product in store to see if it needs restocking.

products = ["soap","shampoo","oil","sugar","rice"]
current_stock = [10,15,16,20,5]
minimum_stock = [5,9,20,15,13]
restock_list = [ ]

for i in range(len(products)):
    if current_stock[i]<minimum_stock[i]:
        restock_list.append(products[i])
        
print("products that needs restocking:")
print(restock_list)