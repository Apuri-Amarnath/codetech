import nltk
from nltk.chat.util import Chat, reflections

# Define some patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am good, how about you?']),
    (r'(.*) your name?', ["I'm a chatbot.", "You can call me a chatbot."]),
    (r'(.*) (age|old) are you?', ["I'm just a computer program, so I don't have an age."]),
    (r'(.*) created you?', ["I was created by a developer.", "I am a product of programming."]),
    (r'quit', ['Bye, take care.', 'Goodbye!']),
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

def main():
    print("Hello! I'm a chatbot. You can start chatting with me. Type 'quit' to end the conversation.")
    # Start the conversation loop
    while True:
        user_input = input("You: ").lower()  # Get user input
        response = chatbot.respond(user_input)  # Get chatbot response
        print("Bot:", response)  # Print chatbot response
        if user_input == 'quit':
            break  # Exit the loop if user inputs 'quit'

if __name__ == "__main__":
    main()
