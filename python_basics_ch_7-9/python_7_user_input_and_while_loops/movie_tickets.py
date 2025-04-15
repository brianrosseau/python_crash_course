movie_intro = "\nWelcome to the Mickey Mouse Movie Theatre!"
movie_intro += "\nWhere we show nothing but Mickey Mouse reruns. How exciting!"
movie_intro += "\nHold your goofy hats, Pluto! First you have to pay for your ticket(s)."
prompt = "\nHow old are you?" 
prompt += "\nPress 'enter' after each age. Type 'quit' when done. \n"

print(movie_intro)

while True:
    age = input(prompt)
    
    if age == 'quit':
        print("Enjoy your movie!")
        break

    age = int(age)

    if age < 3:
        print("Your movie ticket is free!")
    elif age < 13:
        print("Your movie ticket costs $10.")
    else:
        print("Your movie ticket costs $15.")