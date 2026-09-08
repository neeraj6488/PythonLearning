a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is c)
print(a is b)
print(a == b)

def validate_price(price):
    MIN_VALUE = 10.00
    MAX_VALUE = 99.99
    return MIN_VALUE <= price <= MAX_VALUE

print(validate_price(155))

numbers = [1,2,3,4,5]

print(f"is 3 in numbers: {3 in numbers}")

a=1
b=2
c=3
d=4
e=5

print((d*e) or a + b >= c)