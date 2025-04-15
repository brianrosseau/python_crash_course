from pathlib import Path

def multiple_files(path):
    """Reads mulitple files and prints their contents."""
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {filename}")
        print(contents)

filenames = ['cats.txt', 'dogs.txt', 'birds.txt']
for filename in filenames:
    path = Path(filename)
    multiple_files(path)