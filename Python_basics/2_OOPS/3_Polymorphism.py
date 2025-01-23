# Polymorphism: 
print("\nPOLYMORPHISM\n")
class Animal:
    def speak(self):
        return "I make a sound"

class Dog(Animal):  
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for i in animals:
    print(i.speak()) 


