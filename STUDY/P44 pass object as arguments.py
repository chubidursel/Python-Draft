# How to pass object as arguments

class Car:
    color = None

def change_color(car,color):
    car.color = color

class Motorcycle:
    color = None

def change_color(vehicle,color):
    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1, "red")
change_color(car_2, "black")
change_color(car_1, "blue")
change_color(bike_1, "green")

print(car_1.color)
print(car_2.color)
print(car_3.color)

print(bike_1.color)