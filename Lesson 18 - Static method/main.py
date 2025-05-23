'''
Lesson 18 - Static method
@staticmethod 
'''
class  StringManipulator:
    def __init__(self):
        self.a = 1000

    def reverse_string(self, s):
        return s[::-1]
    
    def count_vowels(s):
        vowels = 'aeiouAEIOU'
        return sum(1 for char in s if char in vowels)
    
    def remove_symbols(s):
        return ''.join(char for char in s if char.isalnum() or char.isspace())
    
string = 'Hello World!!!12#@[]'
print(StringManipulator.reverse_string(string, string))
print(StringManipulator.count_vowels(string))
print(StringManipulator.remove_symbols(string))