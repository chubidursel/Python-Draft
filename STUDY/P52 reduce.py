# reduce () = apply a function to an iterable and reduce it to a single cumulative value.
#             performs function on first two elements and repeats process until 1 value remains
# reduce(function, iterable)

import functools

letters = ["H", 'E', "L", 'L', "O"]

word = functools.reduce(lambda x, y,:x+y,letters)
#we combine first 2 letters ["HE", "L", 'L', "O"], than we do it again and again till 1 itereble left
print(word)

#another exemple
factorial  = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y,:x*y,factorial)
#we multiply first 2 numbers [20, 3, 2, 1]
print(result)


#from GG
# importing functools for reduce()
import functools
# importing operator for operator functions
import operator

# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))

# using reduce to compute product
# using operator functions
print("The product (multiply) of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))