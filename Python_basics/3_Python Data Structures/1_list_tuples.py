#Lists and Tuples
#List and Tuple Operations
print("\n(i)LISTS AND TUPLES OPERTIION")
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_list.append(4)
print(my_list) 
my_tuple = my_tuple + (7,)
print(my_tuple)  

#List Comprehensions
print("\n(ii)LIST COMPREHENSIONS")
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

#Nested Lists
print("\n(iii)NESTED LISTS")
nested_list = [[1, 2], [3, 4]]
print(nested_list[1][0]) 

#Tuple Packing and Unpacking
print("\n(iv)TUPLE PACKING AND UNPACKING")
# Tuple packing
my_tuple = 1, 2, 3  
print(my_tuple)     
my_tuple = (1, 2, 3)
print(my_tuple)    
# Tuple unpacking
my_tuple = (4, 5, 6)
a, b, c = my_tuple  
print(a) 
print(b)  
print(c)