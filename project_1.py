# Project 1: Rule-Based AI Chatbot
'''a simple rule based chatbot that can train by pre define ruleswhich can communicate on hi,hello,whats,
'''
# Continuous loop - runs until user exits
while True:

    # Get input from user
    user_input = input("You: ").lower().strip()

    # Handle greetings
    if user_input in ["hello", "hi", "hey","what's up"]:
        print("Bot: Hello! How can I help you?")

    # Handle exit commands
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break  # Exit the loop

    # Handle how are you
    elif user_input == "how are you":
        print("Bot: I'm good, thank you!")

    # Handle name question
    elif user_input in ["what is your name", "who are you"]:
        print("Bot: I am a rule-based chatbot.")

    # Handle unknown input
    else:
        print("Bot: I don't understand that. Try: hello, how are you, bye")