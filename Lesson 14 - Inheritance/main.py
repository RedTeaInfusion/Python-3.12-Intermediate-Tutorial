'''
Lesson 14 - Inheritance
inheritance
super()
'''
class Person:
    def __init__(self, id_number, name):
        self.id = id_number
        self.name = name
    
    def __str__(self):
        return f'Id: {self.id}\nName: {self.name}'
    
class Student(Person):
    def __init__(self, id_number, name, course):
        super().__init__(id_number, name)
        self.course = course

    def __str__(self):
        return super().__str__() + f'\nCourse: {self.course}'
    
class Employee(Person):
    def __init__(self, id_number, name, department):
        super().__init__(id_number, name)
        self.department = department

    def __str__(self):
        return super().__str__() + f'\nDepartment: {self.department}'

student = Student('s123', 'Alice', 'Computer science')
print(student)
employee = Employee('e456', 'Bob', 'HR')
print(employee)
