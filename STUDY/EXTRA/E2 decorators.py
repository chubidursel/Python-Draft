# decorator = a function that takes another function as its argument, and returns yet another function
#   useful as they allow the extension of an existing function, without any modification to the original function source code

# simple example withount @
def decorator(func):
    def inner():
        print("Start decorator..")
        func()
        print("Finished decorator...")
    return inner

def say():
    print("here is the 2nd function")

d = decorator(say)
d()

print('----------- from GG ----------')

# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in // which the argument is called
    # inner function can access the outer local // functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now // inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1

# defining a function, to be called inside wrapper
def function_to_be_used():
    print("***This is inside the function ***")

# passing 'function_to_be_used' inside the >> decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()

print('----------- from GG (2 example)----------')
import time
import math

# decorator to calculate duration (taken by any function)
def calculate_time(func):
    # added arguments inside the inner1, if function takes any arguments can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1

# this can be added to any function present, in this case to calculate a factorial
#           (a function = multiplies a number by every number below it. For example 5!= 5*4*3*2*1=120.)
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time (so that you can see the actual difference)
    time.sleep(3)
    print(math.factorial(num))

# calling the function.
factorial(7)

print("----------- from GG (3 example)----------")
# a function returns something or an argument is passed to the function

def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1

# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b
a, b = 1, 2
# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))