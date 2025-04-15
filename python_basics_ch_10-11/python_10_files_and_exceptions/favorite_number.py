from pathlib import Path
import json

favorite = input("\nWhat is your favorite number? ")

path = Path('favorite.json')
contents = json.dumps(favorite)
path.write_text(contents)

print(f"I'll be sure to remember that your favorite number is {favorite}.\n")
