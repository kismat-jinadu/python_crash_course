prompt="What toppings would you like?"
prompt += "\nEnter 'quit' when you are done choosing: "

message = ''
while True:
    message = input(prompt)

    if message == 'quit':
      break  
    else:
        print(f"\nAdding {message}")