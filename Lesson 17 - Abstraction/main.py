'''
Lesson 17 - Abstraction
abstaction
interface
'''
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 3.14 * self.radius * 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    
shapes = [Circle(3), Rectangle(4,5)]
for shape in shapes:
    print(f'{shape.__class__.__name__} Area: {shape.area()}')
    print(f'{shape.__class__.__name__} Perimeter: {shape.perimeter()}')

