# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of as a shortcut) (useful for short period of time, throw-away)
# lambda parameteres:expression
# multiply = lambda x, y: x * y

def double(x):
    return x * 2
print(double(5))

#same thing but with lambda function
doublebubble = lambda x:x *2
print(doublebubble(20))

multiply = lambda x, y: x * y
print(multiply(7, 3)) # two parameters

add = lambda x, y, z: x + y + z
print(add(6,5,4))

full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Daniel", "smart af"))

age_check = lambda age:True if age >= 18 else False
print(age_check(15))