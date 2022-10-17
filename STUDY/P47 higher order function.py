# Higher order Function = a function that either:
#                       1. accepts a function as an argument
#                       2. return a function (in Pyphon function are also treated as object)

# 1. accepts a function as an argument
def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func): #func is short for function (we put cuz we dont know which of funcions above we gonna use)
    text = func("Hello") #we call 2 function above
    print(text)

hello(loud) #hello = higher order function and passing (loud) in a function as an argument
hello(quiet)


#  2. return a function
def divisor(x): #Higher order Function
    def dividend(y):
        return y / x
    return dividend

divide = divisor(7)
print(round(divide(21)))


# From GG
# Functions can return another function

def create_adder(x):
    def adder(y):
        return x + y

    return adder #2nd we return

add_15 = create_adder(15) #1st we call the main function and put 15 as X
print(add_15(10)) #3rd we call inner function and give 10 as Y

