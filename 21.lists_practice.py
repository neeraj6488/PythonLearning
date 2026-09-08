fruits = ['Apple','Mango','Orange']

print(fruits)

fruits.append("Banana")
print(fruits)

fruits.insert(2,'Cherry')
print(fruits)

fruits.pop(4)
print(fruits)

fruits.sort()
print(fruits)

try:
    print(fruits[10])
except IndexError:
    print("Out of bounds")    

try:
    fruits[10] = 'Guava'
except IndexError:
    print("Not available in the list")    
