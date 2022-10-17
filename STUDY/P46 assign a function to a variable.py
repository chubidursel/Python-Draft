# How to assign a function to a variable

def hello():
    print("Hello")

hi = hello #We're assigning the memmory address of the "hello" to the variable of "hi"
hello()
hi()   #so we can treat hi() as a function

say = print
say("We assigned a function to a variable")

