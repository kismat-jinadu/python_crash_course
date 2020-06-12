odd_numbers=[]
for value in range(1,21,2):
    odd_numbers.append(value)
print(odd_numbers)

multi_three=[]
for value in range(3,30,3):
    multi_three.append(value)
print(multi_three)

cube=[]
for value in range(1,11):
    cube.append(value**3)
print(cube)

cube=[value**3 for value in range(1,11)]
print(cube)
