#Sets
print("\n(iii)SETS")
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)
my_set.remove(3)
print(my_set)
my_set.update([7, 8, 9])
print(my_set)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 | set2  
print(result) 
result = set1 & set2  
print(result)
result = set1 - set2
print(result)

#Set Comprehensions
squares = {x ** 2 for x in range(5)}
print(squares)

#Frozen Sets
set = {1, 2, 3}
set = frozenset(set)
print(set)
set.add(4)  # throws error
print(set)


