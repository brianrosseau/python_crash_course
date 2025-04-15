# Using get() to Access Values

## If the key you ask for doesn't exist, you'll get an error.
## Consider using the get() method instead of the square bracket notation
## if there's a chance the key might not exist.

alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])
## this will produce and error because there is no key called 'points'

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

## if you leave out the second argument in the get() call, Python prints a 
## special value ('None') to indicate the absence of a value. This is not an error.
point_value = alien_0.get('points', )
print(point_value)