'''
from pathlib import Path 
import json

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!\n")
    else:
        username = input("\nWhat is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"\nWe'll remember you when you come back, {username}!\n")
    
greet_user()
'''

# The above code works, but it is doing more than just greeting the user, as
#   the docstring states. It is also retrieving a stored username if one exists.
# Let's refactor greet_user() so it's not doing so many tasks. We'll start by
#   moving the code for retrieving a stored username to a separate function:

'''
from pathlib import Path 
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def greet_user():
    """Greet the user by name"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"\nWelcome back, {username}!\n")
    else:
        username = input("\nWhat is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!\n")

greet_user()
'''

# The function get_stored_username() has a clear purpose. And it is good practice
#   for a function to either return the value you are looking for or return None.
# We should factor one more block of code out of greet_user(). We should move 
#   the code that prompts for a new username to a function dedicated to only that.

from pathlib import Path 
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("\nWhat is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"\nWelcome back, {username}!\n")
    else:
        username = get_new_username(path)
        print(f"\nWe'll remember you when you come back, {username}!\n")

greet_user()

# Now every function in this code has a clear, single purpose. This is important
#   for writing clear code that is easy to maintain and extend.