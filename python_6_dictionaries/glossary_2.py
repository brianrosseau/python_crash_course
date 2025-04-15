## now clean up the code from 'glossary.py' file
## so that you don't have to type a print call for each name
## use for loop instead

programming_words = {
    'variable': 'an object to which a value is assigned',
    'list': 'a collection of items in a particular order', 
    'immutable': 'unchangeable; often refers to values. A tuple is immutable', 
    'conditional test': 'an expression that can be evaluated as True or False',
    'dictionary': 'a collection of key-value pairs',
    }

for key, value in programming_words.items():
    print(f"{key.title()}: \n\t{value}\n")

##since the for loop makes printing so easy, I'll add more terms to the dictionary
programming_words['set'] = 'a collection of unique values'
programming_words

programming_words['string'] = 'a series of characters'
programming_words['integer'] = 'any number that lacks a decimal point'
programming_words['float'] = 'any number that has a decimal point'
programming_words['function'] = 'a block of code that performs a specific task'
programming_words['method'] = '''a function that is associated with an object 
    \tand can manipulate its data or perform actions on it'''

for key, value in programming_words.items():
    print(f"{key.title()}: \n\t{value}\n")