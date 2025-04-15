# EXCEPTIONS
# WORKING WITH MULTIPLE FILES

from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

# Count number of words in 'alice.txt'
path = Path('alice.txt')
count_words(path)


# Create list of text files to run count_words() function.
# Intentionally did not download 'siddhartha.txt' to directory containing 
#   word_count.py to see how well the program handles a missing file. 
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 
             'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)

# the names of the files are stored as simple strings. Each string is then 
#   converted to a Path object, before the call to count_words().
#   The missing file has not effect on the program's execution.


# FAILING SILENTLY
# we can pass over (skip) a file that is not found instead of reporting on it.

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass            # This passes over or skips the missing file
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 
             'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)


#or...
# instead of the pass statement, we can write any missing file names to a 
#  file called 'missing_files.txt'
