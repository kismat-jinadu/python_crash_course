unconfirmed_users=['alice','brian','candance']
confirmed_users=[]

#verify each user until there are no more unconfirmed users.
#move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

#display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())