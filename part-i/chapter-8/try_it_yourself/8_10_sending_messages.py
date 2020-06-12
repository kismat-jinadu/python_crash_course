def send_messages(texts,sent_messages):
    """move text messages to sent messages"""
    while texts:
        pending=texts.pop()
        print(f"Pending message: {pending}")
        sent_messages.append(pending)



def show_messages(sent_messages):
    """Show messages that have been sent"""
    print("\nThe following messages have been sent:")
    for sent_message in sent_messages:
        print(sent_message)

texts=['hi, i am coming over', 'what are you up to?','ok that is fine']
sent_messages =[]

send_messages(texts, sent_messages)
show_messages(sent_messages)
