# --- Functions ---
print("\n(i)DEFINING FUNCTIONS")
def welcome(name):
    return f" {name}, Welcome to Mindpath!"

print(welcome("Naman"))

# Arguments: Positional, Keyword, Default, Arbitrary (*args, **kwargs)
print("\n(ii)Arguments: Positional, Keyword, Default, Arbitrary (*args, **kwargs")
def describe_person(name, age=25, *hobbies, **other_details):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Hobbies: {hobbies}")
    print(f"Other details: {other_details}")

describe_person("Naman", 20, "Reading", "Cycling", city="Delhi", profession="Developer")

# Returning Values
print("\n(iii)RETURNING VALUES")
def add(a, b):
    return a + b
result = print(add(10, 20))

# Variable Scope and Lifetime
print("\n(iv)Variable Scope and Lifetime")
global_var = 9
def local_scope_demo():
    local_var = "I am local"
    print(local_var)
    print(global_var+2)
local_scope_demo()
print(global_var)
# print(local_var)  # throws error

# Lambda Functions
print("\n(v)Lambda Functions")
square = lambda x: x ** 2
print("Square of 5 is: ", square(5))

# First-Class Functions
print("\n(vi)First-Class Functions")
def execute_function(fn, value):
    return fn(value)
print(execute_function(square, 7))

