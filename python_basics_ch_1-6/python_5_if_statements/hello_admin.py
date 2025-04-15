#HELLO ADMIN
usernames = ['brian', 'lorie', 'able', 'angela', 'rob', 'admin']

for user in usernames:
    if user == 'admin':
        print(f"Hello {user.title()}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")

#NO USERS
#add an if test to make sure the list is not empty
#results are same if list is not empty...
usernames = ['brian', 'lorie', 'able', 'angela', 'rob', 'admin']

if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hello {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

#result if list is empty...
usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hello {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")