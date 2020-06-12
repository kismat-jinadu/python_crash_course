responses = {}
question="If you could visit one place in the world,"
question += "where would you go? "
polling_active = True

while polling_active:
    name = input("What is your name? ")
    vacation = input(question)
    responses[name] = vacation
    repeat = input("Would anyone else like to take the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n---Poll Results---")
for name, vacation in responses.items():
    print(f"{name} would like to visit {vacation}.")