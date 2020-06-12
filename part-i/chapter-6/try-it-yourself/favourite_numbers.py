favourite_numbers={
    'john':[9, 16],
    'sam':[4,18],
    'tony':[8, 20],
    'bob':[5, 15],
    'alan':[3, 76]
    }
for person, numbers in favourite_numbers.items():
    print(f"{person}'s favourite numbers are: ")
    for number in numbers:
        print(f"\t{number}")