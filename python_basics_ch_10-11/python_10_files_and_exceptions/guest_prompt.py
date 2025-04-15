from pathlib import Path

prompt = input("Please type your name here: ")

path = Path('guest.txt')
path.write_text(prompt)

