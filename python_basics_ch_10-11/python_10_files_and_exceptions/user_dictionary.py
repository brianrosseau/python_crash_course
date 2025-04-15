from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored user information if available."""
    if path.exists():
        try:
            contents = path.read_text()
            user_info = json.loads(contents)
            return user_info
        except json.JSONDecodeError:
            print("Oops! Something went wrong. Please provide the information again.")
            return None
    else:
        return None

def get_new_user_info(path):
    """Prompt for new user information."""
    user_info = {}
    user_first_name = input("What is your first name? ")
    user_info['First Name'] = user_first_name
    user_last_name = input("What is your last name? ")
    user_info['Last Name'] = user_last_name
    user_birthday = input("What is your birthday? (example: March 22): ")
    user_info['Birthday'] = user_birthday
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def summarize_user_info():
    """Summarizes user information."""
    path = Path('user_info.json')
    user_info = get_stored_user_info(path)
    if user_info:
        print(f'''\nWelcome back!\nHere is a summary of your user information:
              \tFirst Name: {json.dumps(user_info['First Name'])}
              \tLast Name: {json.dumps(user_info['Last Name'])}
              \tBirthday: {json.dumps(user_info['Birthday'])}''')
    else:
        user_info = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_info['First Name']} {user_info['Last Name']}!")


summarize_user_info()


    

'''
user_info = {}

def get_user_first_name(path):
    """Get user first name"""
    user_first_name = input("What is your first name? ")
    user_info['First Name'] = user_first_name
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info
'''