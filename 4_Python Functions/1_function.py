# Functions as Objects
print("\n(i)FUNCTIONS AS OBJECTS\n")
def greet(name):
    return f"Hello, {name}!"
greet_1 = greet  
print(greet_1("Naman")) 

# Storing functions in a list
def add(x, y): return x + y
def multiply(x, y): return x * y
op = [add, multiply]
print(op[0](3, 5))  
print(op[1](3, 5)) 

# Passing Functions as Arguments
print("\n(ii)PASSING FUNCTIONS AS ARGUMENTS\n")
def apply_operation(operation, a, b):
    return operation(a, b)
def add(x, y): 
    return x + y
def multiply(x, y): 
    return x * y
print(apply_operation(add, 3, 5))       
print(apply_operation(multiply, 3, 5))  

#Returning Functions from Functions
print("\n(iii)RETURNING FUNCTIONS FROM FUNCTIONS\n")
def adder(value_to_add):
    def add_to(x):
        return x + value_to_add
    return add_to
add5 = adder(5)  
add10 = adder(10)  
print(add5(7)) 
print(add10(7))  



