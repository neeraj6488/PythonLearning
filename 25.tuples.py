empty_tuples = ()

person = ('Neeraj', 25, 5.2, 'Kharghar')

numbers = 1, 2, 3, 4, 5

print(person)
print(person[2])
print(person[-1])

# Tuple cannot be mutated, meaning once declared we cannot add elements
# numbers[0] = 10 # TypeError: 'tuple' object does not support item assignment

new_numbers = numbers + (11,12,13)
print(new_numbers)

# Packing
coordinates = 10, 20, 30

# Unpacking
x,y,z = coordinates
print(x,y,z)

cnt_numbers = 1, 2, 2, 3, 3, 3, 3, 4
print(cnt_numbers.count(1))
print(cnt_numbers.count(2))
print(cnt_numbers.count(3))

def get_name_age():
    name = 'Neeraj'
    age = 30
    return name, age

result = get_name_age()
print(result)

x, y = get_name_age()
print(x)
print(y)