from pathlib import Path

path = Path('kjv_bible.txt')
contents = path.read_text(encoding='utf-8')

contents.lower().count('the ')

#------------------

def count_common_words(filename, word):
    """Counts how many times word appears in text file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, I could not find the file {filename}")
    else:
        word = word.lower()
        word_count = contents.lower().count(word)
        msg = f"\nThe word '{word}' appears in {filename} about {word_count} times."
        print(msg)


filename = Path('kjv_bible.txt')
count_common_words(path, 'the ')

count_common_words(filename, 'God')

count_common_words(filename, 'love')