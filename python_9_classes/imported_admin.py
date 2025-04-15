# Exercise 9-11b to be used with user_module.py

from user_module import Admin

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