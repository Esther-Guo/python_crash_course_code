def show_messages(messages):
    """print message one by one from a list"""
    print('Showing all messages: ')
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    print('\nSending all messages: ')
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)


messages = ['Hello!', 'Bye!', 'Good afternoon!']
sent_messages = []
show_messages(messages)
send_messages(messages[:], sent_messages) # modified

print(messages)
print(sent_messages)
