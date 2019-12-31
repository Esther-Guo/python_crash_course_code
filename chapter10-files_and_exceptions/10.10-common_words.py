def count_words(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print('File does not exist.')
    else:
        count = content.lower().count(word)
        print(f'The word {word} appears {count} times.')


filename = 'Frankenstein.txt'
count_words(filename, 'the ') # to avoid the count of 'then' 'there'
