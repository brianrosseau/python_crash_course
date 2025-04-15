# Looping through all key-value pairs
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

## The method items() returns a sequence of key-value pairs.
## The for loop saves me from having to type out a print call for each name.

# Looping through all the keys in a dictionary
## the method keys() is useful if you only need to loop through the keys

for name in favorite_languages.keys():
    print(name.title())

## looping through just the keys is the default way of looping a dictionary
## so the result would be the same if the keys() method were not typed...

for name in favorite_languages:
    print(name.title())

## Now we will select specific keys to access...
friends = ['phil', 'sarah']
for name in favorite_languages.keys():              #calling the key
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title() #calling the value; note []
        print(f"\t{name.title()}, I see you love {language}!")

## Next, we will see if someone was polled...
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Looping through a dictionary's keys in a particualr order
## use the sorted() function to sort through the keys in alphabetical order

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping through all values in a dictionary
## the values() method just gives you the values w/o the keys
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
## all the values are printed, even duplicate values

## to avoid duplicates, you can create a set of unique values
## use the set() function
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# SET
## you can build a set directly (different from a list, tuple, or dictionary)
## use curly brackets and separate the elements with commas
languages = {'python', 'rust', 'python', 'c'}
languages

