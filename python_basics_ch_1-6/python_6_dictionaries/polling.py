favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }

potential_pollers = ['sarah', 'timothy', 'phil', 'jessica']

for poller in potential_pollers:
    if poller in favorite_languages:
        print(f"Thank you, {poller.title()}, for taking the poll!")
    else:
        print(f"Hi {poller.title()}, please consider taking the poll.")