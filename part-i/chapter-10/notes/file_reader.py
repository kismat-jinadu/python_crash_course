with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

##  to remove blank lat line in output use rstrip()

print(contents.rstrip())

## can use absolute file path like this:
## file_path = 'part-i/chapter-10/notes/pi_digits.txt'

##with open(file_path) as file_object:
##    contents = file_object.read()
##print(contents)

## reading line by line

file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line)

## strip whitespace

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())


## can store lines as a list within the with block so you can work with it outside the block

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())