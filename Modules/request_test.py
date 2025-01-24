# #Request
print("REQUEST MODULE\n")
import requests
response = requests.get("https://httpbin.org/cookies/set?name=value")
response2 = requests.get("https://jsonplaceholder.typicode.com/posts/1")
response3 = requests.get("https://www.cricbuzz.com/live-cricket-scorecard/100283/ind-vs-eng-1st-t20i-england-tour-of-india-2025/posts")
# print(response.cookies) 
print(response.text)
print(type(response.text))
data = response.json()
data2 = response2.json()
print(data)
print(type(data))
print(data2)
print(type(data2))
print("Server Name1: ",response.headers["Server"])
print("Server Name2: ",response2.headers["Server"])
print("Server Name3: ",response3.headers["Server"])
print("Response Code:",response.status_code)
print("Response Code2:",response2.status_code)
print("Response Code3:",response3.status_code)
print("Response URL:",response.url)
print("Response URL2:",response2.url)
print("Response Encoding:",response.encoding)
print("Response Encoding2:",response2.encoding)
print("Response Reason:",response.reason)
print("Response Reason2:",response2.reason)
print("Response Reason3:",response3.reason)
print("Response Elapsed:",response.elapsed)
print("Response Elapsed2:",response2.elapsed)

#post/delete/update
#request
#itertools - few functions
#pydantic

#POST
print("\nPOST REQUEST\n")
url = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "New Post", "body": "This is a new post.", "userId": 1}
response = requests.post(url, json=data) 
print("Response Code:",response.status_code)
print(response.json())      
print(type(response.json()))


print("\nPOST2 REQUEST\n")
url2 = "https://jsonplaceholder.typicode.com/posts/101"
# data = {"title": "New Post", "body": "This is a new post.", "userId": 1}
response = requests.post(url2) 
print("Response Code:",response.status_code)
print(response.json())      
print(type(response.json()))
#DELETE
print("\nDELETE REQUEST\n")

url = "https://jsonplaceholder.typicode.com/posts/1"  # Resource ID 1
response = requests.delete(url)
print("Response Code:",response.status_code)
if response.status_code == 200:
    print("Resource deleted successfully!")
print(response.json())     

#PUT
print("\nPUT REQUEST\n")
url = "https://jsonplaceholder.typicode.com/posts/1"  # Resource ID 1
updated_data = {"id": 1, "title": "Updated Title", "body": "Updated content.", "userId": 1}

response = requests.put(url, json=updated_data)
print("Response Code:",response.status_code)
print(response.json())  

#PATCH
print("\nPATCH REQUEST\n")
url = "https://jsonplaceholder.typicode.com/posts/1"  # Resource ID 1
updated_data = {"title": "Updated Title"}

response = requests.patch(url, json=updated_data)
print("Response Code:",response.status_code)
print(response.json())

#Query Parameters
print("\nQUERY PARAMETERS\n")
url = "https://httpbin.org/get"
params = {
    "search": "requests library",
    "page": 2
}
response = requests.get(url, params=params)
print("Final URL with query params:", response.url)
print("Response JSON:", response.json())


#Headers
print("\nHEADERS\n")
import requests

response = requests.head("https://httpbin.org/get")
response2 = requests.get("https://httpbin.org/get")
print("Headers:", response2.headers)
print("Status Code:", response.status_code)
print("Headers:", response.headers)


#File Upload
print("\nFILE UPLOAD\n")
url = "https://httpbin.org/post"
files = {
    "file": open("ex.txt", "rb")
}
response = requests.post(url, files=files)
print("Response JSON:", response.json())
