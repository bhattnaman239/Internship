#Basic Exception Handling
print("\n(i)BASIC EXCEPTION HANDLING\n")
try:
    result = "string" + 10 
except TypeError as e:
    print(f"Error: {e}")

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    print(f"Result is {result}")  
finally:
    print("Execution completed!")  
#always runs, irrespective of whether an exception is raised or not

#Custom Exceptions
print("\n(ii)CUSTOM EXCEPTIONS\n")
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(f"Caught: {e}")

class NegativeNumberError(Exception):
    pass

def square_root(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return number ** 0.5

try:
    print(square_root(-1))
except NegativeNumberError as e:
    print(f"Error: {e}")
