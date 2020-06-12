message = input("Tell me something, and I will repeat it back to you:")
print(message)

#let the user choose when to quit

prompt= "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
messsage = ""
while message != 'quit':
    message = input(prompt)
# to prevent the above code from print 'quit', use if statement
    if message != 'quit':
        print(message)