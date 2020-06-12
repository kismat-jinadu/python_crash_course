def count_common_words(filename):
    """Count how many times a particular word in a file"""
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words=contents
        common_word = 'the '
        num_common_words=words.lower().count(common_word)
        print(f"The file {filename} uses the word '{common_word}' {num_common_words} times.")

filename = 'planet_of_no_return.txt'
count_common_words(filename)