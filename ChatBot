import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you."]
    ],
    [
        r"how are you ?",
        ["I'm doing good, how about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind"]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great!"]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, I'm ageless"]
    ],
    [
        r"what do you do?",
        ["I chat with people like you to make your day better."]
    ],
    [
        r"(.*) created you?",
        ["I was created by your name."]
    ],
    [
        r"(.*) (location|city|place)?",
        ["I'm from the digital world. What about you?"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"(.*) favorite color?",
        ["I'm a fan of blue. It reminds me of the vast digital sky."]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon."]
    ],
    [
        r"(.*)",
        ["That's interesting!", "Tell me more!", "I see."]
    ]
]

def chat():
    print("Hi! I am a basic chatbot created by you. Type 'quit' to leave.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    chat()
