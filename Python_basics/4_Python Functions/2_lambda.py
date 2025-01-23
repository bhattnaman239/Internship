# Lambda Expressions
# Anonymous Functions
print("\n(i)ANONYMOUS FUNCTIONS\n")
square = lambda x: x ** 2  
print(square(4))  
add = lambda x, y: x + y  
print(add(3, 5)) 
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(7))  
larger = lambda x, y: x if x > y else y
print(larger(10, 20)) 

# Map, Filter, and Reduce
print("\n(ii)MAP, FILTER, AND REDUCE\n")
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]

from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  
