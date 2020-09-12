import json

with open("7M-friends.json", "rt") as f:
    obj = json.load(f)
    print(obj)
