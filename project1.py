print(" Welcome to AI Chatbot!")
print("Type 'bye' to exit.\n")

responses = {
    "hello": "Hi there 👋",
    "hi": "Hello 😊",
    "how are you": "I am fine. Thanks for asking!",
    "what is your name": "I am an AI Chatbot ",
    "help": "I can chat with you and answer simple questions.",
    "who created you": "I was created by a DecodeLabs intern 😎",
    "good morning": "Good Morning ☀️",
    "good afternoon": "Good Afternoon 🌤️",
    "good evening": "Good Evening 🌙",
    "thank you": "You are welcome 😊",
    "thanks": "Glad to help ",
    "tell me a joke": "Why did the computer go to the doctor? Because it caught a virus ",
    "what can you do": "I can answer basic questions and chat with you.",
    "i am sad": "Don't worry, everything will be okay ",
    "motivate me": "Success comes from consistency and hard work 🚀",
    "bye": "Goodbye! Have a nice day 👋"
}

while True:
    
    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("Bot:", responses["bye"])
        break
    reply = responses.get(
        user_input,
        "Sorry, I don't understand that command "
    )
    print("Bot:", reply)