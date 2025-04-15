languages = ['English', 'Hebrew', 'Greek', 'Turkish', 'Romanian', 'Italian', 'German', 'French', 'Farsi', 'Cantonese', 'Japanese', 'Korean', 'Pig Latin']
print(languages)

languages.append('Spanish')
print(languages)

languages.insert(6, 'Russian')
print(languages)

del languages[9]
print(languages)

popped_language = languages.pop(8)
print(popped_language)
print(languages)

no_time = languages.pop(-2)
print(f"The language I don't have time to learn is {no_time}.")
print(languages)
print(no_time)

forgot = languages.pop(2)
print(f"The language I forgot is {forgot}. Now it's all {forgot} to me.")
print(forgot)
print(languages)

too_gutteral = 'German'
languages.remove(too_gutteral)
print(languages)
print(f'\n{too_gutteral.title()} is too difficult to learn, so "Guten Tag" and farewell.')

# the sort() method is PERMANENT
languages.sort()
print(languages)

languages.sort(reverse=True)
print(languages)

languages.insert(0, 'Portugese')
print(languages)

# the sorted() Function is TEMPORARY
print(sorted(languages))
print(languages)

print(sorted(languages, reverse=True))
print(languages)

# the reverse() method reverses the chronological order of the list (back to front, not alphabetical). It is PERMANENT.
languages = ['English', 'Hebrew', 'Greek', 'Turkish', 'Romanian', 'Italian', 'German', 'French', 'Farsi', 'Cantonese', 'Japanese', 'Korean', 'Pig Latin']
print(languages)

languages.reverse()
print(languages)

languages.reverse()
print(languages)

print("The number of languages in this list is:", len(languages))

print(languages[13]) #Produces index error
print(languages[12])
print(languages[-1])

