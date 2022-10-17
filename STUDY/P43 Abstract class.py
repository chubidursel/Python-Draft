# Prevent a user from creating an object of that class
# + copels a user to override abstract methods a child class

#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but does not an implementation.
#adc - abstract based class

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car!")
    def stop(self):
        print("This car is stoped!")

class Bike(Vehicle):
    def go(self):
        print("You drive the bike!")

    def stop(self):
        print("This bike is stoped!")

#vehicle = Vehicle()
car = Car()
bike = Bike()

#vehicle.go()
car.go()
bike.go()

car.stop()
bike.stop()

