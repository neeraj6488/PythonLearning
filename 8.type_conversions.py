price = '19.99'
price_float = float(price)
quantity = 5
total_cost = price_float * quantity
total_cost_int = int(total_cost)

print(f"Price (string): {price}, Type: {type(price)}")
print(f"Price (float): {price_float}, Type: {type(price_float)}")
print(f"Quantity (int): {quantity}, Type: {type(quantity)}")
print(f"Total Cost (float): {total_cost}, Type: {type(total_cost)}")
print(f"Total Cost (int): {total_cost_int}, Type: {type(total_cost_int)}")

