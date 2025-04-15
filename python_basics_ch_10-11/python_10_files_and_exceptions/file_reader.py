from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

# or...
path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()        # Removes the empty blank line after the output
print(contents)

# or...
path = Path('pi_digits.txt')
contents = path.read_text().rstrip()  # strips the trailing new line character
print(contents)


#----------------------
path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(lines)

# or can skip the variable 'lines' for simpler code...
for line in contents.splitlines():
    print(lines)