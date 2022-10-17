import math

pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi)) #negative to positive
print(pow(pi,2))
print(math.sqrt(pi))
print(max(x,y,z,))
print(min(x,z,y))
print(" ")
print('My own math / practice')
print(z+y*pi-2)
print(21/7+x-y*2+pi)

# ----------------from CODEWARS!!!--------------
#inbuilt function sum() which sums up the numbers in the list.
def sum_array(a):
    Sum = sum(a)
    print(Sum)
a= [21,35,54,-2,2.5]

# a function that does four basic mathematical operations.
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1+value2
    if operator == '-':
        return value1-value2
    if operator == '*':
        return value1*value2
    if operator == '/':
        return value1/value2
print(basic_op("*", 4, 5))
#return eval("{}{}{}".format(value1, operator, value2))
#return eval(str(value1) + operator + str(value2))
#!!!!The eval() method parses the expression passed to this method and runs python expression (code) within the program.

# ODD OR EVAl(/2)
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

# odd or even (sum of the list)
def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'
arr = [21,4,55,21]
print(oddOrEven(arr))

#------------Most Digits from List in Python-------------
def find_longest(arr):
    return max(arr, key=lambda x: len(str(x)))
arr = [100, 9, 10, 300, 99, 9999]
print(find_longest(arr))