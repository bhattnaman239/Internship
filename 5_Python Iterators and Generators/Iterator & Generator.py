# Iterators and Iterables
print("\n(i)ITERATORS AND ITERABLES\n")
my_list = [1, 2, 3, 4]
my_iterator = iter(my_list)
print(next(my_iterator)) 
print(next(my_iterator)) 
print(next(my_iterator))
print(next(my_iterator))

#Generators
print("\n(ii)GENERATORS\n")
def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

a = my_generator()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# print(next(a))  # error

def my_generator():
    for i in range(5):
        yield i
a = my_generator()
for i in a:
    print(i)
