prompt="What toppings would you like?"
prompt += "\nEnter 'quit' when you are done choosing: "

message = ''
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(f"\nAdding {message}")
    else:
        print("Thank you and wait for the waiter")
