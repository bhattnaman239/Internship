#Regex module
print("REGEX MODULE\n")
import re
user= input("Enter a string: ")
a=input("Enter a pattern to search: ")
result = re.search(rf"{a}", user)
if result:
    print("Match found:", result.group())  # Output: Match found: Hello
else:
    print("No match")

result = re.match(r'\d+', '123abc')
if result:
    print(f'Matched: {result.group()}')
else:
    print('No match')

#FINDALL
print("\nFINDALL:")
result = re.findall(rf"{a}", user)
print(result)  

#SUB
print("\nSUB:")
a= "I like cats and cats are cute."
print("Original String:",a)
result = re.sub(r"cats", "dogs", a)
print("SUB: ",result)  

#SPLIT
print("\nSPLIT:")
result = re.split(r" ",a)
print(result)

#FINDITER
print("\nFINDITER:")
result = re.finditer(r"cats", a)
for i in result:
    print(i)

