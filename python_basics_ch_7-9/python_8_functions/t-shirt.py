def make_shirt(size, message):
    """Summarizes the size of the shirt and the message printed on it."""
    print(f"You ordered a size {size} shirt with the message: {message}.")

make_shirt('M', 'I am a Gospel Project')                # positional arguments
make_shirt(size='M', message='I am a Gospel Project')   # keyword arguments
make_shirt(message='I am a Gospel Project', size='M')   # order doesn't matter when using keyword arguments

# Large Shirts
#  Modify the function defintion so that the shirt size is large by default

def make_shirt(message, size='Large'):
    """Summarizes the size of the shirt and the message printed on it."""
    print(f"You ordered a size {size} shirt with the message: {message}.")

make_shirt('I love Python')

#  Modify the function again, this time with a default message as well.
def make_shirt(message='I love Python', size='Large'):
    """Summarizes the size of the shirt and the message printed on it."""
    print(f"You ordered a size {size} shirt with the message: {message}.")

make_shirt()        #this produces the default size and default message
make_shirt(size='Medium')   # this produces the default message but overrides the default size
make_shirt(size='Small', message='I am a Gospel Project')   # this overrides both the default size and default message
