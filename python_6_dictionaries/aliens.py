# NESTING
# 1. A List of Dictionaries (dictionaries inside a list)

## One way to manage a whole fleet of aliens is to create a dictionary about
## each alien and then store each dictionary in a list. We can then loop
## through the list and print out each alien.
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

## But three aliens is not a realistic fleet... how about thirty!
## Let's create code that automatically generates thirty green aliens, 
## using the range() function.

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first five aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

## The thirty aliens all have the same characteristics, but Python considers
## each one a separate object, which allows us to modify each alien individually

## For example, to change the first three aliens to yellow, medium-speed, worth
## ten points each, we could do this...
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first five aliens
for alien in aliens[:5]:
    print(alien)
print("...")
## Only the first three aliens have changed

## We could the loop by adding an elif statement that turns yellow aliens red...
for alien in aliens[0:6]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:10]:
    print(alien)
print("...")
