# Passing an Arbitrary Number of Arguments to a function (continued)

# Using Arbitrary Keyword Arguments
# the double asterisks (**) tells Python to create a dictionary containing all 
#   the extra name-value pairs the function recieves.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)