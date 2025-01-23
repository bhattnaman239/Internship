#JSON
print("JSON\n")
import json

with open(r"C:\Users\mtisqa\Desktop\data.json", "r") as file:
    data = file.read()
    print(data)
    print(type(data))

python_obj = {"name": "Alice", "age": 25}

with open("data.json", "w") as file:
    json.dump(python_obj, file)
