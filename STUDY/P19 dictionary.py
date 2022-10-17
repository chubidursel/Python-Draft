# dictionary = a changeable, unordered collection of unique key:value pairs
            # fast because they use hashing, allow us to access a value quickly

capitals = {"USA":"WDC",
            "India":"New Dehli",
            "China":'Beijung',
            "Russia":'Moscow'}
capitals.update({"Germany":'Baerlin'}) #add another key/value
capitals.update({"USA":"NYC"}) #update one of the key
capitals.pop('China')#remove this key

print(capitals["Russia"]) #Russia - key / Moscow - value
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key, value)

# Pythontoday Youtube
person = {"name":"Daniel",
          "age":25,
          "weight":75,
          "you phone":"iphone",
          "sport":"chess"}
print(person["name"]) #print only 1 key
print(person)
for k,v in person.items():
    print(f"{k} >>> {v}")   #nice way to show up the list
