# #Request
print("REQUEST MODULE\n")
import requests
response = requests.get("https://httpbin.org/cookies/set?name=value")
response2 = requests.get("https://jsonplaceholder.typicode.com/posts/1")
response3 = requests.get("https://www.cricbuzz.com/live-cricket-scorecard/100283/ind-vs-eng-1st-t20i-england-tour-of-india-2025/posts")
print(response.cookies) 
print(response.text)
data = response.json()
data2 = response2.text
print(response2.text)
print(data)
print(data2)
print(response.headers["Server"])
print(response2.headers["Server"])
print(response.status_code)
print(response2.status_code)
print(response3.status_code)
print("Response URL:",response.url)
print("Response URL2:",response2.url)
print("Response Encoding:",response.encoding)
print("Response Encoding2:",response2.encoding)
print("Response Reason:",response.reason)
print("Response Reason2:",response2.reason)
print("Response Reason3:",response3.reason)
print("Response Elapsed:",response.elapsed)
print("Response Elapsed2:",response2.elapsed)

