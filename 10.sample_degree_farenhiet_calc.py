# This is the Celsius to Fahrenheit Temperature values.
# Author: Neeraj Deshbhratar
# Version: 1.0
# Date: 07 Sep 2026
from calendar import month

days_in_week = 7
temp_in_celsius = 40.0
pi = 3.14159

user_name = "Neeraj"
is_summer = True
month = ["January", "February", "March", "April"]

temp_scales = {"Celsius" : "°C", "Fahrenheit" : "°F"}

celsius_to_fahrenheit_factor = 9 / 5
fahrenheit_offset = 32

fahrenheit_temp = (temp_in_celsius * celsius_to_fahrenheit_factor) + fahrenheit_offset
fahrenheit_temp = round(fahrenheit_temp, 1)

greetings = "Greetings " + user_name

month_count = len(month)

output = str(temp_in_celsius) + temp_scales["Celsius"] + " is equal to " + str(fahrenheit_temp) + temp_scales["Fahrenheit"]

output2 = f"{temp_in_celsius}{temp_scales['Celsius']} is equal to {fahrenheit_temp}{temp_scales['Fahrenheit']}"

print(greetings)
print(f"No of months count: {month_count}")
print(output)
print(output2)
print(f"Is this summer {is_summer}")
print(f"There are {days_in_week} days in week")
print(f"Value of pi is {pi}")

