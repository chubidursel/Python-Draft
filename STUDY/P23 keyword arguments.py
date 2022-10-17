# keyword arguments = arguments preceded (предшествовал) by identifier when  we pass them to a function
#                         The order of the arguments doesn't matter, unlike positional arguments
#                       Python knows the name of the arguments that our function receives
#                          (shortened to kwargs)

def hello(first, middle,last):
    print("Hey! "+first+middle+last)

hello(middle="is ", first="Daniel ", last="cool")

#from W3
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Alex", child2 = "Max", child3 = "Dan")


def team(name, project):
    print(name, "is working on an", project)


team("Danya", "Python")