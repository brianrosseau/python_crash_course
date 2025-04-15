# A Dictionary of Similar Objects
## The alien_0.py file used a dictionary to store different kinds of 
## information about one object, an alien in a game.
## Now we will use a dictionary to store one kind of information about many
## objects. 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
## Notice that we use a separate line for each key-value pair

## Now let's look up Sarah's favorite language...
## (creating a variable makes for a much cleaner print call)
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

