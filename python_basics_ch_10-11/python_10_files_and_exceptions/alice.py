from pathlib import Path

path = Path('alice.txt')
contents = path.read_text(encoding='utf-8')

# the above produces a FileNotFoundError because
#   the file 'alice.txt' is not saved the same file as 'alice.py'

from pathlib import Path

path = Path('alice.txt')
# write a try-except block to avoid the FileNotFoundError
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

#-------------------------------
# Let's download the text of Alice in Wonderland from Project Gutenburg online.
# I saved it as text file 'alice.txt' and put it in the same directory as 'alice.py'
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8') # One long string of the entire book
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()        # Split the 'contents' string into a list of all the words in the book.
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

# the above code counts all the words in the text file 'alice.txt'.

