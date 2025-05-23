'''
Lesson 12 - Class
class
attributes
methods
'''
values = list()
values.append(10)
values.remove(10)
print(values)
print(type(values))

class Calculator:
    def __init__(self, result=0):
        self.result = result

    def add(self, value):
        self.result += value

    def subtract(self, value):
        self.result -= value

    def get_result(self):
        return self.result
    
calc = Calculator()
calc.add(10)
calc.subtract(4)
print(calc.get_result())
print(type(calc))