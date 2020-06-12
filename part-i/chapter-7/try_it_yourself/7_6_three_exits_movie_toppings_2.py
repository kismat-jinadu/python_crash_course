prompt= "\nHow old are you?"
prompt += "\nEnter 'quit' to end "

active = True

while active:
    age = input(prompt)
    if age != 'quit':
        age = int(age)

        if age <=3:
            print(f"\tThe ticket is free")
        elif 3<age<12:
            print(f"\tThe ticket is $10")
        elif age >= 12:
            print(f"\tThe ticket is $15")
    if age == 'quit':
        active = False
        print(f"\tProceed to purchase ticket.")