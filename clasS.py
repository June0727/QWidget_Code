from typing import Any


class Human:
    def __init__(self, n):
        self.name = n
        
    def print_name(self):
        print(self.name)
        return self.name
        
a = Human('Ji June Bae')

class Student(Human):
    def __init__(self):
        super().__init__('not defined')

b = Student()

class Teacher(Human):
    def __init__(self, n):
        super().__init__(n)
    
    def print_name(self):
            print('teacher:', self.name)
        
a = print