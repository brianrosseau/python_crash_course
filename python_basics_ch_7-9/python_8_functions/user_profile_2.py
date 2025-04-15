def build_profile(first, last, **user_info):
    """Build a dictionary containing everthing we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('brian', 'rosseau',
                             city='macon',
                             state='georgia',
                             zip_code='31220')
print(user_profile)