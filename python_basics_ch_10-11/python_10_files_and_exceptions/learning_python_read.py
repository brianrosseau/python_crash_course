from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

print(contents)

lines = contents.splitlines()
learning_string = ''
for line in lines:
    learning_string += line
    learning_string += ' '

print(learning_string)