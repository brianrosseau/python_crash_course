from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()      #lstrip() removes the whitespace that was on the left side of the digits on each line

print(pi_string)
print(len(pi_string))


# Large Files: One Million Digits
path = Path('pcc_3e-main/pcc_3e-main/chapter_10/reading_from_a_file/pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))



# Birthday in pi   (see also pi_birthday.py)
contents = path.read_text()
print(contents[:52])

birthday = input("\nEnter your birthday, in the form mmddyy: ")
if birthday in contents:
    print("\nYour birthday appears in the first million digits of pi!\n")
else:
    print("\nYour birthday does not appear in the first million digits of pi.\n")