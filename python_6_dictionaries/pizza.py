# NESTING (continued)
# 2. A List in a Dictionary (list inside a dictionary)

## Instead of making a list of dictionaries (dictionaries inside a list),
## as we did in file aliens.py, sometimes it's helpful to put a list inside
## a dictionary.

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

#-------------------------
# let's apply this to the dictionary from favorite_languages.py
# we can have a lists of several favorite languages with the dictionary...

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c',],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for lang in languages:
        print(f"\t{lang.title()}")

## Note in the for loop above that 'languages' in line 1 is the variable for values
## in the dictionary favorite_languages. Inside that for loop is another for loop
## in which 'languages' (which are lists) are looped through.

## We can refine this code further with an if statement that delineates between
## those with one or more than one favorite language.
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"{name.title()}'s favorite languages are:")
    else:
        print(f"{name.title()}'s favorite language is:")
    
    for lang in languages:
        print(f"\t{lang.title()}")


