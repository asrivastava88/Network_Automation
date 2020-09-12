import json


friends = {"Nikhil": [28, "Pune", 4211215], "Ninad": [
    32, "Pune", 4244215], "AK": [32, "Aurangabad", 45445471], "Khushi": [32, 'Pune', 474474744]}

with open("7M-friends.json", "w") as f:
    json.dump(friends, f, indent=4)

json_str = json.dumps(friends, indent=4)
print(json_str)
