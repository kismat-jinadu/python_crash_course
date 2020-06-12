filename= 'programming_poll.txt'

poll_active = True

while poll_active is True:
    poll = input("Why do you like programming? ")
    print("Thank you for your response.")
    with open(filename,'a') as file_object:
        file_object.write(f"{poll}\n")

    add_poll = input(f"Would anyone else like to participate in this poll? yes/no.\n")
    if add_poll == 'yes':
        poll_active = True
    elif add_poll == 'no':
        print("Poll complete")
        break
        poll_active = False