def count_words(filename):
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
    #count the approximate number of words in the file. 
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames =['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


## you can make python fail silently by adding pass

def count_words(filename):
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
    #count the approximate number of words in the file. 
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames =['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)