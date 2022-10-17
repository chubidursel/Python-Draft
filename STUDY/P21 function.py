# A function is a block of code which only runs when it is called.

#def hello(name):
#    print("Hi! "+name)
#    print("Have a nice day!")

#name = "Daniel" # argument
#hello(name)

def hello(f_name, l_name, age):
    print("Yo! "+f_name+''+l_name)
    print("You are "+str(age)+' years old')
    print("Fck of!")

hello("Dan", "FFF", 21)
#if your function expects 2 arguments,
# you have to call the function with 2 arguments, not more, and not less.



def my_function(fname):
  print(fname + " KKK")


my_function("Emil")
my_function("Tobias")
my_function("Linus")
#The following example has a function with one argument (fname).
# When the function is called, we pass along a first name,
# which is used inside the function to print the full name:

