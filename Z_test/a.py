# import json
# import os
# import requests

# # def save_user_data_to_json(username, email, filename):
# #     data = {"username": username, "email": email}

# #     # Check if the file exists
# #     if os.path.exists(filename):
# #         with open(filename, "r") as f:
# #             try:
# #                 users = json.load(f)  # Load existing data
# #                 if not isinstance(users, list):
# #                     users = []
# #             except json.JSONDecodeError:
# #                 users = []
# #     else:
# #         users = []

# #     users.append(data)  # Append new user

# #     # Save back to file
# #     with open(filename, "w") as f:
# #         json.dump(users, f, indent=4)

# # # Example usage
# # save_user_data_to_json("alice", "alice@example.com", "users.json")
# # save_user_data_to_json("bob", "bob@example.com", "users.json")

# # 2
# import requests
# import time

# session = requests.Session()

# # Time without session
# start = time.time()
# for _ in range(5):
#     requests.get("https://httpbin.org/get")  # Opens & closes 5 connections
# print("Without Session:", time.time() - start)

# # Time with session
# start = time.time()
# for _ in range(5):
#     session.get("https://httpbin.org/get")  # Reuses the connection
# print("With Session:", time.time() - start)


import requests

def post_json_data(url, data_dict):
    response = requests.post(url, json=data_dict)
    
    if response.status_code >= 200 and response.status_code < 300:
        return response.json()  # Successful request
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

# Example Usage
try:
    response_data = post_json_data("https://httpbin.org/post", {"name": "Alice"})
    print(response_data)
except Exception as e:
    print(e)
