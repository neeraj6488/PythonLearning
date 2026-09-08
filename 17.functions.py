# Type Conversions
my_list = [1,'two', 3.5, [4, 5]]

number = "123"
integer = int(number)
float_num = 12.75

print(min(integer, float_num))
print(max(integer, float_num))
print(sum((integer, float_num)))

for item in my_list:
    print(f"The type of {item} is {type(item)}")

message = "Hello, world"
words = message.split(", ")
print(words)

print(", ".join(word.lower() for word in words))

fruits = ["apple", "banana", "cherry"]

print("|".join(fruits))

print("".join(reversed(message)))
print("".join(message.upper()))