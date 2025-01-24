#JSON
print("JSON\n")
import json

#Converting JSON to Python
print("\nCONVERTING JSON TO PYTHON\n")
a= '{"age": 25,"name": "Alice","city":"New York"}'
b= json.loads(a)
print(b)
print(type(b))

#Converting Python to JSON
print("\nCONVERTING PYTHON TO JSON\n")
obj = {"name": "Alice", "age": 25}
json_string = json.dumps(obj, indent=4)
print(json_string)

#Separators
print("Separators")
json_string = json.dumps(obj, separators=(",", ";"))
print(json_string)

#Writing JSON (python data into json file with indentation and sorting keys)
print("\nWRITING JSON\n")
# with open(r"C:\Users\mtisqa\Desktop\data.json", "w") as file:
with open("d.json", "w") as file:
    json.dump(obj,file, indent=2, sort_keys=True)
    print("Data written successfully")

#Reading JSON
print("\nREADING JSON\n")
with open(r"C:\Users\mtisqa\Desktop\data.json", "r") as file:
    data = file.read()
print(data)
print(type(data))


#Reading JSON (json file into python data)
with open("d.json", "r") as file:
    n = json.load(file)
print(n) 
print(type(n))


import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()  
print(data["title"])  
print(data) 
print(type(data))  