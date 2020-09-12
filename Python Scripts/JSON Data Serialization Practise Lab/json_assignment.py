import requests
from collections import Counter
import json

url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)

data = response.json()
print(data)

print("\n")

for task in data:
    if task['userid'] == True:
        print(task)

count = len(task)
print(count)
