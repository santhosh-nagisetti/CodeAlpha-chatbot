import streamlit as st
import nltk
import string
from faq_data import faqs

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
# ---------------------------
# Text Preprocessing Function
# ---------------------------
def preprocess(text):
    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [
        word for word in tokens
        if word not in string.punctuation
    ]

    stop_words = set(stopwords.words('english'))

    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    return " ".join(tokens)

# ---------------------------
# Prepare FAQ Data
# ---------------------------
questions = list(faqs.keys())
answers = list(faqs.values())

processed_questions = [
    preprocess(q) for q in questions
]

vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(
    processed_questions
)

# ---------------------------
# Chatbot Function
# ---------------------------
def get_answer(user_question):
    processed_input = preprocess(
        user_question
    )

    user_vector = vectorizer.transform(
        [processed_input]
    )

    similarities = cosine_similarity(
        user_vector,
        faq_vectors
    )

    best_match_idx = similarities.argmax()

    confidence = similarities[0][best_match_idx]

    if confidence > 0.2:
        return answers[best_match_idx]
    else:
        return (
            "Sorry, I couldn't find a relevant answer."
        )

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖"
)

st.title("🤖 FAQ Chatbot")

st.write(
    "Ask a question related to AI, ML, NLP, or Streamlit."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )

# User Input
user_input = st.chat_input(
    "Ask your question..."
)

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    response = get_answer(user_input)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)