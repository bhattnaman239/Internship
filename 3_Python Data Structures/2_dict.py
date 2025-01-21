#Dictionaries
#Dictionary Methods
print("\n(i)DICTIONARIES METHODS")
my_dict = {"name": "Naman", "age": 21}
print(my_dict["name"])  
my_dict["city"] = "Greater Noida"
print(my_dict)
print(my_dict.keys()) 
print(my_dict.values())
print(my_dict.items())  

#Nested Dictionaries
print("\n(ii)NESTED DICTIONARIES")
nested_dict = {
    'student1': {'name': 'Naman', 'age': 20, 'grade': 'A'},
    'student2': {'name': 'Bhatt', 'age': 22, 'grade': 'A+'}
}
print(nested_dict['student2']['age'])  
nested_dict['student1']['city'] = 'New York'
print(nested_dict['student1'])  

nested_dict['student3'] = {'name': 'Charlie', 'age': 19, 'grade': 'B'}
print(nested_dict['student3'])  

#Dictionary Comprehensions
print("\n(iii)DICTIONARY COMPREHENSIONS")
squares = {x: x ** 2 for x in range(5)}
print(squares)