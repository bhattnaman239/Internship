# Classes and Objects
print("\nCLASSES AND OBJECTS\n")
class Person:
    def __init__(self, name, age):  
        self.name = name 
        self.age = age

    def greet(self):  
        return f"Hello, my name is {self.name}."

person1 = Person("Naman", 20) 
print(person1.greet())  
