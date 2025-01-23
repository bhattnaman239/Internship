# Inheritance
print("\nINHERITANCE\n")
class Animal:
    def speak(self):
        return "I make a sound"

class Dog(Animal):  
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

print(Animal().speak())
print(Dog().speak())
print(Cat().speak())