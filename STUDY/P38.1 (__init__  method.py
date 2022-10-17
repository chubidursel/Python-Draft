# A Sample class with init method
#This method is called when an object is created from a class and
# it allows the class to initialize the attributes of the class.

class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

        # Sample Method

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Daniel')
p.say_hi()

#From W3

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
#The __init__() function is called automatically every time
# the class is being used to create a new object.

