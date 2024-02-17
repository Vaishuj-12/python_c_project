import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm doing well, thank you!", "I'm good, thanks for asking."]),
    (r"what is your name?", ["My name is Vbot.", "You can call me Vbot."]),
    (r"who created you?", ["I was created by a Vaishnavi."]),
    (r"(.*) your name(.*)", ["My name is Vbot."]),
    (r"(.*) (age|old) are you(.*)", ["I am just a computer program, so I don't have an age."]),
    (r"(.*) (location|located) are you(.*)", ["I exist in the virtual world, so I don't have a physical location."]),
    (r"(.*) (weather|temperature) today(.*)", ["I'm sorry, I am not capable of providing weather information."]),
    (r"(.*) (thank you|thanks)(.*)", ["You're welcome!", "No problem."]),
    (r"bye|goodbye", ["Goodbye!", "Bye!", "Take care!"])
]
chatbot = Chat(patterns, reflections)

def main():
    print("Welcome! I'm Chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == "bye":
            break

if __name__ == "__main__":
    main()
