# map() = applies a functions to each item in an iterable (list, tuple, etc.)
#
#map (function, iterable)

store = [("shirt", 20.0),
         ('pants', 25.00),
         ("bra", 88),
         ("socks", 5.00)]

# how convert precises from $ to Euro
to_euros = lambda data: (data[0], data[1]*0.82)

#                   map(function, iterable)
store_euros = list(map(to_euros, store))    #use used list() to convert this object to an itereble

for i in store_euros:
    print(i)


#from W3
def myfunc(n):
  return len(n)

x = list(map(myfunc, ('apple', 'banana', 'cherry')))
print("How many letters in ech word from W3:")
print(x)


#from GG
# Python program to demonstrate working of map.

# Return double of n
def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(addition, numbers) # We double all numbers using map()
print(list(result))

# Double all numbers using map and lambda (!same shit but easy)
numbers = (2, 4, 8, 10)
result = map(lambda x: x + x, numbers)
print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)


#from Programiz

numbers = [2, 4, 6, 8, 10]

# returns square of a number
def square(number):
  return number * number

# apply square() function to each item of the numbers list
squared_numbers_iterator = map(square, numbers)

# converting to list
squared_numbers = list(squared_numbers_iterator)
print(squared_numbers)

#-----------CODEWARS-----------
#You get an array of numbers, return the sum of all of the positives ones.
def positive_sum(arr):
    arr = map(abs, arr)
    return sum(arr)
arr = [5, -4, 2, -7]
print(positive_sum(arr))