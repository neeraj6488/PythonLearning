# Managing a shopping list and grocery items
# 1. Checking if an itme is in the list
# 2. Adding an item to the list
# 3. Removing an item from the list
# 4. Accessing an item by index
# 5. Modifying the quantity of an item in the nested grocery list

# Shopping list
shopping_list = ['milk', 'eggs', 'bread', 'cheese', 'apples']

print("Shopping List: ")
print(shopping_list)

item_to_check = input("Enter item to search: ")

if item_to_check in shopping_list:
    print(f"{item_to_check} is available in the list")
else:
    print(f"{item_to_check} is not available in the list")

new_item = input("Enter an item to add: ")
shopping_list.append(new_item)
print(f"Added {new_item} to the list")
print(shopping_list)

remove_item = input("Enter an item to remove: ")
if remove_item in shopping_list:
    shopping_list.remove(remove_item)
    print(f"Removed {new_item} from the list")
    print(shopping_list)
else:
    print(f"Item {remove_item} is not available in the list")

index = int(input("Enter the index position to check: "))

try:
    print(f"The index position {index} has item {shopping_list[index]}")
except IndexError:
    print(f"The index passed is out of bounds")