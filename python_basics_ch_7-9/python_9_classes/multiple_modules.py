# Exercise 9-12c to be used with user_only_module.py and priv_admin_module.py

# Exercise that imports classes from two modules

# import from each module separately
from user_only_module import User
import priv_admin_module


user_0 = Admin('brian', 'rosseau', 'brosseau', 'brosseau@yoyo.com')
print(user_0.describe_user())

# No current privileges...
user_0.privileges.show_privileges()

# Add privileges...
user_0_privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    ]

# instance.class.attribute
user_0.privileges.privileges = user_0_privileges
user_0.privileges.show_privileges()