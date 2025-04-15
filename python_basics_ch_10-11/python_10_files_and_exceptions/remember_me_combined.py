from pathlib import Path 
import json

path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"\nWelcome back, {username}!\n")
else:
    username = input("\nWhat is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!\n")
    