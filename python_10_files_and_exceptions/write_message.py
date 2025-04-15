# WRITING TO A FILE
from pathlib import Path

# Writitg a single line
path = Path('programming.txt')
path.write_text("I love programming.")
# even though the file 'programming.txt' did not exist, write_text() 
#  created the file and wrote text into it. It also properly closes the file.


# Writing multiple lines
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)
# note: the new write_text() replaces the single line one above.
#   if I were to run the single line one again, it would replace this one.
#   (see programming.txt)




