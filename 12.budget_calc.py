# Calculate the budget
total_budget = 1500
gas_cost = 600
food_cost = 300
accomodation_cost = 200
souvenier_cost = 25

total_expenses = gas_cost + food_cost + accomodation_cost

remaining_money = total_budget - total_expenses

number_of_souveniers = remaining_money // souvenier_cost
money_left_after_souveniers = remaining_money % souvenier_cost

print(f"Total expenses for the trip comes to {total_expenses} out of {total_budget}")
print(f"Money left to buy souveniers is {remaining_money}")
print(f"Total {number_of_souveniers} number of souveniers can be bought from remaining money")
print(f"Money left after buying {number_of_souveniers} is {money_left_after_souveniers}")