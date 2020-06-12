squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

#or
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

#digits=[1,2,3,4,5,6,7,8,9,0]
# min(digits) will output 0
# max(digits) will output 9
# sum(digits) will output 45

# use of list comprehension for similar output as codes above

squares=[value**2 for value in range(1,11)]
print(squares)