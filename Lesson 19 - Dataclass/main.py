'''
Lesson 19 - Dataclass
dataclass
@property
'''
from dataclasses import dataclass
import math

@dataclass
class Point:
    x: int
    y: int = 0

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    @property
    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

p1 = Point(3, 4)
print(p1)
p2 = Point(2, 2)
print(p1.distance_to(p2))
print(p1.distance_from_origin)