import json

filename = 'user_number.json'

number = input("What is your favourite number? ")

with open(filename, 'w') as f:
    json.dump(number,f)
    