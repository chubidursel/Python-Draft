#Function annotations are arbitrary (random) python expressions that are associated with various part of functions.
# [RUS]полезные подсказки


# The -> int just tells that f() returns an integer (but it doesn't force the function to return an integer).
#   It is called a return annotation, and can be accessed as f.__annotations__['return'].
def f(x) -> int:
    return int(x)
x = 15.6
print(f(x))


#v: float tells people who read the program (and some third-party libraries/programs, e. g. pylint) that x should be a float.
# It is accessed as f.__annotations__['x'], and doesn't have any meaning by itself.
def f(y: float) -> int:
    return int(y)
y = 114.5
print(f(y))