# Duck typing = concept where the class of an object is less important that the methods/attributes
#               class type is not checked if minimum method/attributes are present
#               If it walks like a duck, and it quacks like a duck, then it must be a duck.

class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is qwuacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("This chicken is clucking")
class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()   #object of that class
chicken = Chicken()
person = Person()

person.catch(chicken)  #If the person will its catch method
# we pass chicken as an argument (even our parameter is set up to take a duck)
