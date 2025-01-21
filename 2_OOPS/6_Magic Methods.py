#Magic Methods
print("\nMAGIC METHODS\n")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# Magic method for +
    def __add__(self, other):  
        return Point(self.x+ other.x, self.y + other.y)
 # Magic method for str()
    def __str__(self):  
        return f"({self.x }  , {self.y})"

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
# Magic method for <
    def __lt__(self, other):  
        return self.price < other.price

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2 
print(p3) 
s1="naman "
s2="bhatt"
s3=s1+s2
print(s3)

product1 = Product("Product A", 30)
product2 = Product("Product B", 50)
print(product1 < product2)  # True

