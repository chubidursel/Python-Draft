# multiple inheitance = when a child class is derived from more than one parent class.
class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print('This animal is hunting')

class Rabbit(Prey):
    def flee(self): #method overwring (from the parent class)
        print("This rabbit is running away from a wolf")

class Hawk(Predator):
    pass
class Fish(Prey, Predator): #!can obtain both classes
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

hawk.hunt()
rabbit.flee()
fish.flee()