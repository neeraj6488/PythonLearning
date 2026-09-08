person = {
    'name' : 'Neeraj', 'age' : 30, 'city' : 'Kharghar'
}

print(person['name'])
print(person['age'])

person['email'] = 'neeraj6488@gmail.com'
print(person['email'])
person['age'] = 38
print(person['age'])

del person['city']
print(person)

for key in person:
    print(key,person[key])

for value in person.values():
    print(value)

for key, value in person.items():
    print(key,value)


for key in person:
    print(f"{key} is {person[key]}")