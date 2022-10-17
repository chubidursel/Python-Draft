# *args = parameter that will pack all arguments into a tuple
#          useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3, 5, 6, 7))

#we can renaname whatever u want
def add(*staff):
    sum = 0
    stuff = list(staff)
    stuff[0] = 0
    for i in staff:
        sum += i
    return sum

print(add(1,2,3,4,5))

# !!! from Real Python
# sum_integers_list.py
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))
