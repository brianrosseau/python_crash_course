from pathlib import Path
import json

path = Path('favorite_remembered.json')
if path.exists():
    contents = path.read_text()
    favorite = json.loads(contents)
    print(f"\nI know your favorite number! It's {favorite}.\n")
else:
    favorite = input("\nWhat is your favorite number? ")
    contents = json.dumps(favorite)
    path.write_text(contents)
    print(f"I'll be sure to remember that your favorite number is {favorite}.\n")