current_users = ['bob', 'stu', 'wendy', 'wilma', 'tom', 'jack', 'jill']

new_users = ['rumplestilskins', 'repunsel', 'jack', 'jill', 'princess']

for user in new_users:
    if user in current_users:
        print("Sorry, that username is in use. Your will have to select a new username.")
    else:
        print("That username is available.")

#but Python is case-sensitive
#what if one of the new_user names if all caps
current_users = ['bob', 'stu', 'wendy', 'wilma', 'tom', 'jack', 'jill']

new_users = ['rumplestilskins', 'repunsel', 'jack', 'JILL', 'princess']

for user in new_users:
    if user in current_users:
        print("Sorry, that username is in use. Your will have to select a new username.")
    else:
        print("That username is available.")


#need to account for case-sensitive usernames
current_users = ['bob', 'stu', 'wendy', 'wilma', 'tom', 'jack', 'Jill']

new_users = ['rumplestilskins', 'repunsel', 'jack', 'JILL', 'princess']

#current_lower = current_users[:]

current_lower = [user.lower() for user in current_lower]

for user in new_users:
    if user.lower() in current_lower:
        print("Sorry, that username is in use. Your will have to select a new username.")
    else:
        print("That username is available.")

