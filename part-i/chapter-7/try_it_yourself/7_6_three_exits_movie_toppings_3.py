prompt= "\nHow old are you?"
prompt += "\nEnter 'quit' to end "

while True:
    age = input(prompt)
    
    if age == 'quit':
        print(f"\tProceed to purchase ticket.")
        break
    else:
        age = int(age)

        if age <=3:
            print(f"\tThe ticket is free")
        elif 3<age<12:
            print(f"\tThe ticket is $10")
        elif age >= 12:
            print(f"\tThe ticket is $15")
        