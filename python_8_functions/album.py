# Exercises 8-7 and 8-8

# Exercise 8-7
def make_album(artist_name, album_title):
    """Builds a dictionary describing a music album"""
    album = {'artist': artist_name, 'album': album_title}
    return album

album_1 = make_album('Rich Mullins', 'Winds of Heaven, Stuff of Earth')
print(album_1)

album_2 = make_album('Michael W Smith', 'i 2 (EYE)')
print(album_2)

album_3 = make_album('Margaret Becker', 'The Reckoning')
print(album_3)


# Modify the function and add an optional parameter
def make_album(artist_name, album_title, number_of_songs=None):
    """Builds a dictionary describing a music album"""
    album = {'artist': artist_name, 'album': album_title}
    if number_of_songs:                                 # Add if statement
        album['number_of_songs'] = number_of_songs
    return album

album_1 = make_album('Rich Mullins', 'Winds of Heaven, Stuff of Earth')
print(album_1)

album_2 = make_album('Michael W Smith', 'i 2 (EYE)', number_of_songs=11)
print(album_2)

album_3 = make_album('Margaret Becker', 'The Reckoning', 11)
print(album_3)


# Exercise 8-8: User Albums
def make_album(artist_name, album_title):
    """Builds a dictionary describing a music album"""
    album = {
        'artist': artist_name, 
        'album': album_title
        }
    return album

while True:
    print("\nPlease enter the artist's name and the title of the album: ")
    print("(enter 'q' at any time to quit)")

    name = input("Artist name: ")
    if name == 'q':
        break

    title = input("Album title: ")
    if title == 'q':
        break

    user_album = make_album(name, title)
    print(user_album)

print("\nThank you for responding!")
