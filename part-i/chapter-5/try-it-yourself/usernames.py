usernames=['admin','elmanto','kismacik','kjin','scooby']
for username in usernames:
    if username=='admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again")

usernames=[]
if usernames:
    for username in usernames:
         print(f"Hello {username}, thank you for logging in again")
else:
    print("We need to find some users!")

current_users=['andy','mike','pam','dwight','jim']
new_users=['ross','rachel','phoebe','pam','jim']
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} taken. Please choose another username")
    else:
        print(f"{new_user} available")