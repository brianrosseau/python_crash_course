players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)

#first element is the index number to start at. Second element is the index to stop BEFORE (does not include that index number). It is the index to go up to but not to include.
print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

print(players[-3:])

#third element tells how many to skip
print(players[0:4:2])

print(players[:4:2])

print(players[-4:-1:2])

#using a for loop
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())