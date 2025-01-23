#Static and Class Methods
print("\nSTATIC AND CLASS METHODS\n")
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

print(Calculator.add(5, 3))  # 8
print(Calculator.subtract(10, 7))  # 3

# Class Methods
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def number_of_objects(cls):
        return cls.count
    
person1 = Person("Naman")
person2 = Person("Bhatt")
print(Person.number_of_objects())  
