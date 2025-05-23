'''
Lesson 13 - Dunder methods
class attribute
instance attribute
constructor
__str__
__del__
'''
class Book:
    counter = 0
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        Book.counter += 1
    
    def __str__(self):
        return f'{self.title} by {self.author} {self.year}'

    def __del__(self):
        Book.counter -= 1
        print(f'Book {self.title} has been deleted')

book1 = Book('1984', 'George Orwell', 1949)
print(book1)
book2 = Book('Under the skin', 'Michel Faber', 2000)
print(book2)
print(Book.counter)
del book1
print(Book.counter)