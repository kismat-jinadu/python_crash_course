print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")


first_number = input("\nFirst number: ")

second_number = input("Second number: ")
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("You can only add integers")
else:
    print(answer)