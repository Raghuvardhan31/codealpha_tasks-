Chatbot Using Natural Language Processing
This project is a simple chatbot built using Python, leveraging libraries like NLTK, spaCy, and scikit-learn. The chatbot can respond to predefined questions and provide meaningful answers using TF-IDF Vectorization and Cosine Similarity for matching user inputs to predefined questions.

Features
Processes user input using natural language preprocessing.
Matches user queries to predefined questions using similarity metrics.
Provides responses for a wide range of topics, including Python, AI, machine learning, and more.
Offers a conversational interface with the ability to exit the chat anytime.
Requirements
To run this project, ensure the following are installed:

Python 3.x
Libraries:
nltk
spacy
scikit-learn
Installation
Clone this repository or copy the script into a .py file.
Install the required libraries:
bash
Copy code
pip install nltk spacy scikit-learn
Download the NLTK data:
python
Copy code
import nltk
nltk.download('punkt')
Download the spaCy language model:
bash
Copy code
python -m spacy download en_core_web_sm
Usage
Run the script:
bash
Copy code
python chatbot.py
Start a conversation by typing your query.
Type exit to end the chat.
Code Explanation
1. Predefined Questions and Answers
A dictionary qa_pairs contains predefined questions and their respective answers.
These serve as the knowledge base for the chatbot.
2. Text Preprocessing
The preprocess function uses spaCy to:
Convert text to lowercase.
Remove stopwords and punctuation.
Perform lemmatization to reduce words to their base forms.
3. Finding the Best Response
The get_response function:
Preprocesses user input and predefined questions.
Uses TF-IDF Vectorization to calculate the similarity between the input and questions.
Returns the most relevant response if the similarity exceeds a threshold (default: 0.3).
4. Chatbot Interaction
The chatbot function provides a loop for continuous interaction.
Users can exit the chat by typing exit.
Example Interaction
plaintext
Copy code
Chatbot: Hi there! Type 'exit' to end the chat.
You: What is Python?
Chatbot: Python is a versatile programming language used for web development, data analysis, AI, and more.
You: Tell me a joke.
Chatbot: Why don't programmers like nature? It has too many bugs!
You: Bye.
Chatbot: Goodbye! Have a great day!