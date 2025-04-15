players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)

print("The first three players in the list are:")
for player in players[:3]:
    print(player.title())

print("Three players in the middle of the list are:")
for player in players[1:4]:
    print(player.title())

print("The last three players in the list are:")
for player in players[-3:]:
    print(player.title())

