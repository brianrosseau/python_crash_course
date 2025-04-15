from pathlib import Path 
import json

path = Path('favorite.json')
contents = path.read_text()
favorite = json.loads(contents)

print(f"\nI know your favorite number! It's {favorite}.\n")