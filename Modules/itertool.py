#Itertool
print("\nITER TOOL\n")
import itertools

letters = ['A', 'B', 'C']
numbers = [1, 2]
prod = itertools.product(letters, numbers)
print(list(prod))

#Permutations and Combinations
print("\nPERMUTATIONS AND COMBINATIONS\n")
items = ['A', 'B', 'C']
perms = itertools.permutations(letters, 2)  
print("Perms: ",list(perms))

comb = itertools.combinations(letters, 2)  
print("Comb: ",list(comb))

#Infinite Iterators
print("\nINFINITE ITERATORS\n")
count = itertools.count(start=1, step=2)
print(next(count))
print(next(count))
print(next(count))
print(next(count))


#Cycle
print("\nCYCLE\n")
cycle = itertools.cycle(letters)
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

#Chain
print("\nCHAIN\n")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = itertools.chain(list1, list2)
print(list(combined))

import itertools
import operator

#Accumulate
print("\nACCUMULATE(Sum & Product)\n")
nums = [1, 2, 3, 4,5]
cumulative_sums = itertools.accumulate(nums)
print(list(cumulative_sums))

cumulative_product = itertools.accumulate(nums, operator.mul)
print(list(cumulative_product))

#Groupby
print("\nGROUPBY\n")
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 30},
    {'name': 'Dexter', 'age': 30},
]

grouped = itertools.groupby(data, key=lambda x: x['age'])
for key, value in grouped:
    print(key, list(value))

