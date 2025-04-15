
'''
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()
'''
# the above code fails the test 'test_name_function_2.py' when running pytest
# to avoid this, we make the middle name optional and run pytest again

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()