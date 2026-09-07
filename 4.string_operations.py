greeting = "Hello, World!"
name = "Neeraj"

print(len(greeting))
print(greeting[0])
print(greeting[2])
print(greeting[-1])

print()

print(name[1:4]) # eer
print(name[0:6:2]) # Nea
print(name[::-1]) # jareeN
print(name[::-2]) # jre

full_name = name + " Deshbhratar"
chant = name * 3
print(full_name)
print(chant)
print(full_name.upper())
print(greeting.lower())
print(name.replace("e","x"))