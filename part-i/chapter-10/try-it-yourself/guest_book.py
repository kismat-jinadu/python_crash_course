
filename = 'guest_book.txt'

guest_checkin = True

question = "What is your name? "

while guest_checkin is True:
    name=input(question)
    print(f" Hello {name}. Welcome to our home")
    with open(filename,'a') as file_object:
        file_object.write(f"{name.title()}\n")
    
    more_guests = input("Are there more guests in your party? yes/no ")
    if more_guests == 'yes':
        guest_checkin = True
    elif more_guests == 'no':
        print("Proceed to the living room")
        break
        guest_checkin = False
        

