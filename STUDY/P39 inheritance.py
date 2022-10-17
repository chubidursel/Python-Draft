#inheritance
#inher (наследовать)

class Animal:
    alive = True

    def eat(self):
        print("This aninimal is eating")

    def sleep(self):
        print("This aninimal is sleeping")

class Rabbit(Animal):
    def run(self):   #unique attributes/method
        print('This rabbit is running')

class Fish(Animal):
    def swim(self):
        print('This fish is swimming')

class Hawk(Animal):
    def fly(self):
        print('This hawk is flying')

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()
