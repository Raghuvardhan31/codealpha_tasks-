import nltk
import spacy
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data
nltk.download('punkt')

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Predefined questions and answers

qa_pairs = {
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm just a bot, but I'm here to help you!",
    "what is your name": "I am a simple chatbot created to assist you.",
    "bye": "Goodbye! Have a great day!",
    "what can you do": "I can answer your questions and help you with basic tasks.",
    "who created you": "I was created by a developer who loves Python and chatbots!",
    "what is python": "Python is a versatile programming language used for web development, data analysis, AI, and more.",
    "what is nltk": "NLTK stands for Natural Language Toolkit. It's a Python library for processing human language data.",
    "what is spacy": "spaCy is a powerful Python library for advanced natural language processing.",
    "tell me a joke": "Why don't programmers like nature? It has too many bugs!",
    "how do i learn python": "Start with online tutorials, practice coding, and build projects to improve your skills.",
    "what is ai": "AI, or Artificial Intelligence, is the simulation of human intelligence in machines.",
    "what is machine learning": "Machine learning is a subset of AI that enables machines to learn from data and improve over time.",
    "what is your purpose": "My purpose is to assist you and make your life easier by answering your questions.",
    "what is chatbot": "A chatbot is a program designed to simulate conversation with human users.",
    "what is the weather": "I'm not connected to live weather data, but you can check a weather app for updates!",
    "how old are you": "I was created recently, so I'm quite young in bot years!",
    "what is programming": "Programming is the process of writing instructions for a computer to execute.",
    "what is your favorite color": "I don't have eyes, but I think blue is a calming color!",
    "can you help me": "Of course! Let me know what you need help with.",
    "what is the time": "I'm not connected to a clock, but you can check your device for the current time.",
    "do you like humans": "Yes! I exist to assist humans and make their lives easier.",
    "what is openai": "OpenAI is a research organization focused on developing and promoting AI for the benefit of humanity.",
    "what is the capital of france": "The capital of France is Paris.",
    "who is the president of the usa": "As of my programming, the current president is Joe Biden. This may change over time.",
    "how do i make a chatbot": "You can use Python libraries like NLTK, spaCy, and frameworks like Flask or Django.",
    "what is deep learning": "Deep learning is a type of machine learning that uses neural networks to model and solve complex problems.",
    "what is data science": "Data science involves analyzing and interpreting complex data to make informed decisions.",
    "what is cloud computing": "Cloud computing is the delivery of computing services over the internet.",
    "what is blockchain": "Blockchain is a distributed ledger technology used for secure and transparent transactions.",
    "what is the internet": "The internet is a global network that connects millions of private, public, academic, business, and government networks.",
    "what is a computer": "A computer is an electronic device that processes and stores data to perform tasks.",

}

# Preprocess text using spaCy
def preprocess(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

# Find the best response using cosine similarity
def get_response(user_input):
    user_input = preprocess(user_input)
    questions = list(qa_pairs.keys())
    preprocessed_questions = [preprocess(q) for q in questions]

    # Use TF-IDF to calculate similarity
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([user_input] + preprocessed_questions)
    similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    # Find the best match
    best_match_index = similarities.argmax()
    if similarities[best_match_index] > 0.3:  # Threshold for similarity
        return qa_pairs[questions[best_match_index]]
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"

# Chatbot function
def chatbot():
    print("Chatbot: Hi there! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
