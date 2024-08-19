from abc import ABC, abstractmethod

# Implementation Interface
class Color(ABC):
    @abstractmethod
    def apply_color(self):
        pass

# Concrete Implementation Classes
class Red(Color):
    def apply_color(self):
        print("Applying red color")

class Blue(Color):
    def apply_color(self):
        print("Applying blue color")

# Abstraction Interface
class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

    def apply_color(self):
        self.color.apply_color()

# Refined Abstraction Classes
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")
        self.apply_color()

class Square(Shape):
    def draw(self):
        print("Drawing a square")
        self.apply_color()

# Client Code
if __name__ == "__main__":
    red = Red()
    blue = Blue()

    circle = Circle(red)
    square = Square(blue)

    circle.draw()
    square.draw()