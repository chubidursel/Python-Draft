# scope = The region that a variable is recognized
# объем    A variable is only avalible from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "Daniel"     #global scope (available inside/outside)
def display_name():
    name = "KKK"     # local scope (available only inside this function)
    print(name)

print(name)
display_name()

# from W3

x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
print(x)

