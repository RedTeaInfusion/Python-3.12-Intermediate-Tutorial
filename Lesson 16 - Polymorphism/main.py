'''
Lesson 16 - Polymorphism
polymorphism
method overloading
'''
class Shape:
    def area(self):
        return 'Area not defined'
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
circle = Circle(5)
rectangle = Rectangle(2, 3)
shape = Shape()
shapes = [circle, rectangle, shape]
for s in shapes:
    print(f'Area: {s.area()}\n'
          f'Is a Shape: {isinstance(s, Shape)}\n'
          f'Is a Circle: {isinstance(s, Circle)}\n'
          f'Is a Rectangle: {isinstance(s, Rectangle)}\n')