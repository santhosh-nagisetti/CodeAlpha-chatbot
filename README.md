# CodeAlpha-chatbot
#  FAQ Chatbot using NLP & Streamlit

##  Project Overview

This project is an FAQ Chatbot built using Python, NLP, and Streamlit. The chatbot answers user questions by finding the most similar question from a predefined FAQ dataset and returning the corresponding answer.

The project uses Natural Language Processing (NLP) techniques such as text preprocessing, tokenization, stopword removal, TF-IDF vectorization, and cosine similarity to understand user queries and provide relevant responses.

---

##  Features

* Interactive chatbot interface using Streamlit
* FAQ-based question answering system
* Text preprocessing using NLTK
* TF-IDF Vectorization
* Cosine Similarity for question matching
* Chat history support
* Beginner-friendly implementation

---

##  Technologies Used

* Python
* Streamlit
* NLTK
* Scikit-learn

---

##  Project Structure

```text
FAQ-Chatbot/
│
├── s2.py
├── requirements.txt
└── README.md
```

---

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/FAQ-Chatbot.git
cd FAQ-Chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run s2.py
```

---

##  How It Works

1. User enters a question.
2. The text is preprocessed using NLP techniques.
3. FAQ questions are converted into TF-IDF vectors.
4. Cosine similarity is calculated between the user's question and stored FAQs.
5. The most similar FAQ is selected.
6. The chatbot displays the corresponding answer.

---

##  Example Questions

* What is AI?
* What is Machine Learning?
* What is Deep Learning?
* What is NLP?
* What is Streamlit?

---

## 📸 Output

The chatbot provides instant responses through a simple and interactive Streamlit chat interface.

---

## 📚 Learning Outcomes

* Natural Language Processing fundamentals
* Text preprocessing techniques
* Similarity matching using cosine similarity
* Building web applications with Streamlit
* Implementing FAQ-based chatbots

---

## 👨‍💻 Author

Santhosh Nagisetti

CodeAlpha Internship Project
