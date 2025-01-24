import requests

url = "https://httpbin.org/get"
params = {
    "search": "requests library",
    "page": 2
}
response = requests.get(url, params=params)
print("Final URL with query params:", response.url)
print("Response JSON:", response.json())
