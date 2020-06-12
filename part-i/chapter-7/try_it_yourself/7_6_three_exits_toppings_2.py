prompt="What toppings would you like?"
prompt += "\nEnter 'quit' when you are done choosing: "

message = ''
active = True
while active:
    message = input(prompt)
    
    if message =='quit':
        active = False
        print("Thank you and wait for the waiter")
    else:
        print(f"\nAdding {message}")
        