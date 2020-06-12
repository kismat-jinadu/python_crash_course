import json

filename = 'user_number.json'

with open(filename) as f:
    number = json.load(f)
    print(f"I know your favourite number! It's {number}.")