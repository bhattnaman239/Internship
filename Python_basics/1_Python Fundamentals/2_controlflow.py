# --- Control Flow ---
print("\n(i)CONDITIONAL STATEMENTS")
value = 10
if value > 0:
    print("Positive number")
elif value == 0:
    print("Zero")
else:
    print("Negative number")


print("\n(ii)LOOPS")
# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 3:
    print(count)
    count += 1

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"Nested Loop: {i} {j}")

# Looping through a list
my_list = [1, 2, 3]
for i in my_list:
    print(i)

# Iterators and Iterables
print("\n(iii)ITERATORS AND ITERABLES")
list = [1, 2, 3]
list1 = iter(list)
print(next(list1))
print(next(list1))
print(next(list1))


# Break statement
print("\n(iv)BREAK AND CONTINUE STATEMENTS")
for i in range(5):
    if i == 3:
        break
    print(i)

# Continue statement
for i in range(5):
    if i == 3:
        continue
    print(i)

