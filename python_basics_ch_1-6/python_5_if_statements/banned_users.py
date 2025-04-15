#CHECKING WHETHER A VALUE IS IN A LIST
# USE KEYWORD 'IN'
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings

'pepperoni' in requested_toppings


#CHECKING WHETHER A VALUE IS NOT IN A LIST
# USE KEYWORD 'NOT'

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

