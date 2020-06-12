import json

filename = 'user_number_2.json'

try:
    with open(filename) as f:
        number=json.load(f)
except FileNotFoundError:
    number = input("What is your favourite number? ")
    with open(filename, 'w') as f:
        json.dump(number,f)
print(f"I know your favourite number! It's {number}.")
    