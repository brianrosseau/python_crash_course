'''
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""                 # Be sure to define message with an empty string so it has some comparison to start with.
while message != 'quit':
    message = input(prompt)
    print(message)
'''
# the above code works well, except it prints the word 'quit' as if it were
# an actual message.
# an if statement can fix this...

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""                 # Be sure to define message with an empty string so it has some comparison to start with.
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':       # Insert if statement
        print(message)
