def count_words(filename):
    """Count how many words in a file"""
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words=contents.split()
        num_words=len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['cats.txt','dogs.txt']
for filename in filenames:
    count_words(filename)   