# filter () = cretes a collectoin of elements from an iterable for which a function returns true
#
# filters(function, iterable)

friends = [("Dan", 25),
           ("Ann", 13),
           ("Max", 21),
           ("Joe",7),
           ("Bob", 77)]

age = lambda data:data[1] >=18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)

#from W3
#same as example before but without lambda
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)

#from Programiz

letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# a function that returns True if letter is vowel
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False

filtered_vowels = filter(filter_vowels, letters)

# converting to tuple
vowels = tuple(filtered_vowels)
print(vowels)