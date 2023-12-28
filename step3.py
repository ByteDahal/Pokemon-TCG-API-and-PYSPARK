import json
with open(r"response.json", "r")as file:
    a = json.load(file)
print(a)