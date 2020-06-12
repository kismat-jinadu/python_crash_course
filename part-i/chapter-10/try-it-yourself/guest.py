name = input("What is your name? ")

filename= 'guest.txt'

with open(filename,'w') as file_object:
    file_object.write(f"{name.title()}\n")
    