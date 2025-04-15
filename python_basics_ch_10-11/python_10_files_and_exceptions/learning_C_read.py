message = "I really like dogs!"
message.replace('dog', 'cat')

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

print(contents)


lines = contents.splitlines()
learning = ''
for line in lines:
    learning += line
    learning += ' '

print(learning.replace('Python', 'C'))


# Simpler Code
# can skip the temporary variable 'lines'
learning = ''
for line in contents.splitlines():
    learning += line
    learning += ' '

print(learning.replace('Python', 'C'))