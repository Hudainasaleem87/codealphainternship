import nltk
from nltk.stem import WordNetLemmatizer
import random

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

intents = [
    {
        "tag": "greeting",
        "patterns": ["hello", "hi", "hey", "is anyone there", "good morning", "good evening", "moin"],
        "responses": ["hello there, general kenobi", "hi there, how can i help?", "is there anything i can help you with today?"]
    },
    {
        "tag": "goodbye",
        "patterns": ["cya", "see you later", "bye", "good bye", "have a nice day"],
        "responses": ["see you later, bye!", "have a nice day", "bye! come back again you will be missed"]
    },
    {
        "tag": "thanks",
        "patterns": ["thanks", "thank you", "that's helpful", "appreciate it", "thanks a lot"],
        "responses": ["you're welcome", "anytime!", "no problem", "you got it"]
    },
    {
        "tag": "about",
        "patterns": ["who are you?", "what are you?", "what is your name?", "about you"],
        "responses": ["I am a chatbot, created to help you. Ask me anything!", "I am an AI, here to answer your questions."]
    },
    {
        "tag": "abilities",
        "patterns": ["what can you do?", "what are your skills", "what you can do for me"],
        "responses": ["I can answer your questions, assist with tasks, and provide information."]
    },
    {
        "tag": "help",
        "patterns": ["help", "i need help"],
        "responses": ["I can help you with a variety of tasks. How can I assist you today?"]
    },
    {
        "tag": "sorry",
        "patterns": ["sorry", "apologies", "i apologize"],
        "responses": ["It's okay", "No worries", "It happens"]
    },
    {
        "tag": "unknown",
        "patterns": ["*", "?", "what", "who", "how", "why"],
        "responses": ["I don't understand. Can you please rephrase that?", "I'm still learning. Could you ask that differently?"]
    }
]

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
    return tokens

def get_response(text):
    results = []
    for intent in intents:
        for pattern in intent['patterns']:
            if pattern in text:
                results.append({
                    'intent': intent['tag'],
                    'score': 1
                })
    if len(results) == 0:
        results.append({'intent': 'unknown', 'score': 0})
    return random.choice(results)['intent']

def chatbot_response(text):
    intent = get_response(preprocess_text(text))
    for intent in intents:
        if intent['tag'] == intent:
            return random.choice(intent['responses'])

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)