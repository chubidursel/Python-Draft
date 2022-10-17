# Object oriented programming (POOP)
#is a style of programming characterized by the identification of classes of objects
# closely linked with the methods (functions) with which they are associated.

from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford", 'Mustang', 2022,'red')

#print(car_2.make)
#print(car_2.model)
#print(car_2.year)
#print(car_1.color)
print(car_2.make,car_2.model,car_2.year,car_2.color )

car_2.drive()
car_2.stop()

#car_1.wheels = 2       #We can change information here
#Car.wheels = 3
print(car_1.wheels)
print(car_2.wheels)