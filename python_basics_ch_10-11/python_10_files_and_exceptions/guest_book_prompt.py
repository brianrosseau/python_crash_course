from pathlib import Path

prompt = "\nPlease enter guest's name here "
prompt += "\n(Enter 'q' when all guests are entered.):  "

guest_book = ''
while True:
    name = input(prompt)

    if name == 'q':
        if guest_book:
            path = Path('guest_book.txt')
            path.write_text(guest_book)
            print(f"\nThe following names have been added to the guestbook: \n{guest_book}")
            break
        else:
            path = Path('guest_book.txt')
            path.write_text("There are no names in the guestbook.")
            print(f"\nThere are no names in the guestbook.\n")
            break
    else:
        guest_book += name
        guest_book += '\n'

