# Exercises 8-9, 8-10, and 8-11

# Exercise 8-9
# Start with a list of short text messages
text_messages = ['Headed home now.', 'Love you!', 'Hi Beautiful!']

# Pass the list to a function that prints each text message.
def show_messages(messages):
    """Prints each message in the list of messages."""
    for message in messages:
        print(message)

show_messages(text_messages)

# or format the printed messages by adding tabs...
def show_messages(messages):
    """Prints each message in the list of messages."""
    print("The following messages are in the list of messages.")
    for message in messages:
        print(f"\t{message}")

show_messages(text_messages)


# Exercise 8-10
text_messages = ['Headed home now.', 'Love you!', 'Hi Beautiful!']
sent_messages = []                                      # Add empty list

def send_messages(text_messages, sent_messages):        # Add another function
    """
    Simulate printing each message until none are left.
    Move each printed message to sent_messages list.
    """
    while text_messages:
        current_message = text_messages.pop(0)
        print(f"Message being printed: {current_message}")
        sent_messages.append(current_message)


def show_messages(messages):
    """Prints each message in the list of messages."""
    print("The following messages are in the list of messages.")
    for message in messages:
        print(f"\t{message}")

send_messages(text_messages, sent_messages)
show_messages(sent_messages)

# Check to make sure the messages have been moved.
print(text_messages)            # Now the text_message list is the empty one
print(sent_messages)            # And they have all been moved to the sent_messages list


# Exercise 8-11
# Start with code from Exercise 8-10
text_messages = ['Headed home now.', 'Love you!', 'Hi Beautiful!']
sent_messages = []                                      # Add empty list

def send_messages(text_messages, sent_messages):        # Add another function
    """
    Simulate printing each message until none are left.
    Move each printed message to sent_messages list.
    """
    while text_messages:
        current_message = text_messages.pop(0)
        print(f"Message being printed: {current_message}")
        sent_messages.append(current_message)

def show_messages(messages):
    """Prints each message in the list of messages."""
    print("The following messages are in the list of messages.")
    for message in messages:
        print(f"\t{message}")

# Call the function with a copy of the list, in order to retain the original.
send_messages(text_messages[:], sent_messages)

# Print both lists to make sure the original text_message list is still there.
print(text_messages)
print(sent_messages)
