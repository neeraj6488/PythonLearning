groceries = [
    ['milk', 2],
    ['bread', 7],
    ['egg', 6],
    ['tea', 3],
    ['coffee', 5]
]

print(groceries[0][0])

for item, quantity in groceries:
    print(item,quantity)

modify_item = input("Enter the item to modify: ")
item_found = False

for i, (item,quantity) in enumerate(groceries):
    if item == modify_item:
        no_to_add = int(input("Enter the qunatty to be added: "))
        groceries[i][1] = no_to_add
        item_found = True
        break

if item_found:
    print("Quantity updated:")
    for (item,quantity) in groceries:
        print(f"{quantity} for {item}")
else:
    print(f"{modify_item} not available in the list")
