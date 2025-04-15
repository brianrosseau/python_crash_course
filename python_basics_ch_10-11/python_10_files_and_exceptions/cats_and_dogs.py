from pathlib import Path

def multiple_files(path):
    """Reads mulitple files and prints their contents."""
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"...Sorry, I can't find the file {path}")
    else:
        print(contents)

filenames = ['cats.txt', 'dogs.txt', 'birds.txt']
for filename in filenames:
    print(f"\nReading file: {filename}")
    path = Path(filename)
    multiple_files(path)

