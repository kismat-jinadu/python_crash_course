lottery_active = True
numbers=range(1,11)
pick= ['a','d','f','g','m']
my_ticket = ['d',2,4,'g']
counter=0

while True:
    counter +=1
#merge the numbers and letters
    for number in numbers:
        if number not in pick:
            pick.append(number)

    from random import choice 

    select_1 = choice(pick)
    select_2 = choice(pick)
    select_3 = choice(pick)
    select_4 = choice(pick)

    winning_ticket= [select_1,select_2,select_3,select_4]

    if winning_ticket == my_ticket:
        break
        lottery_active = False
        counter = counter
    
print(f"You played {counter} times before winning the lottery")



