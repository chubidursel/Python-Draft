# super() = Function used to give access to the methods of a parent class.
            # Returns a tempotrary object of a parent class when used

class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

class Square(Rectangle):
    def __init__(self, lenght, width):
        super().__init__(lenght, width)
    def area(self):
        return self.lenght*self.width

class Cube(Rectangle):
    def __init__(self, lenght, width, height):
        super().__init__(lenght, width)
        self.height = height
    def volume(self):
        return self.lenght*self.width*self.height

square = Square(3, 5)
cube = Cube(3, 4, 3)

print(square.area())
print(cube.volume())
