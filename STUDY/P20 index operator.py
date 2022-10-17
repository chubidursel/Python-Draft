# index operator [] = gives acces to a sequence's element (str, list, tuples)

name = "daniel"

if(name[0].islower()):
    name = name.capitalize()
print(name)


fisrt_name = name[0:5].upper()
last_name = name[4:].lower()
last_character = name[-1]

print(fisrt_name)
print(last_name)
print(last_character)