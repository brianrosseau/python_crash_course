from pathlib import Path

path = Path('pcc_3e-main/pcc_3e-main/chapter_10/reading_from_a_file/pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("\nEnter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("\nWinner! Your birthday appears in the first million digits of pi!\n")
else:
    print("\nSorry, your birthday does not appear in the first million digits of pi. No pie for you!\n")



'''
# The following also works: no need to use splitlines()

contents = path.read_text()
print(contents[:52])

birthday = input("\nEnter your birthday, in the form mmddyy: ")
if birthday in contents:
    print("\nYour birthday appears in the first million digits of pi!\n")
else:
    print("\nYour birthday does not appear in the first million digits of pi.\n")

'''