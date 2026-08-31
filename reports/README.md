# 😊 AI Sentiment Analysis Dashboard

An AI-powered Natural Language Processing application that analyzes text and classifies sentiment as positive, negative, or neutral.

---

## 🚀 Project Overview

Understanding customer opinions and feedback is important for businesses and organizations.

This project uses Natural Language Processing to analyze text and identify the sentiment expressed in customer reviews, feedback, comments, and other text data.

The system provides interactive sentiment analytics and allows users to analyze individual text or upload CSV datasets.

---

## 🧠 Natural Language Processing Approach

The system analyzes the emotional polarity of text.

### Sentiment Classes

- 😊 Positive
- 😞 Negative
- 😐 Neutral

### Polarity Range

```text
-1.0 → Strongly Negative
 0.0 → Neutral
+1.0 → Strongly Positive
```

---

## ✨ Features

- Individual text sentiment analysis
- Customer feedback analysis
- Positive sentiment detection
- Negative sentiment detection
- Neutral sentiment detection
- Sentiment polarity scores
- Interactive analytics dashboard
- CSV upload
- Batch sentiment analysis
- Sentiment distribution visualization

---

## 🛠️ Technologies Used

- Python
- Natural Language Processing
- TextBlob
- Pandas
- NumPy
- Plotly
- Streamlit

---

## 📁 Project Structure

```text
AI-Sentiment-Analysis-Dashboard/
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── app.py
│
├── data/
│   └── README.md
│
├── src/
│   └── sentiment_analyzer.py
│
├── models/
│   └── README.md
│
├── notebooks/
│   └── README.md
│
└── reports/
    └── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Sentiment-Analysis-Dashboard.git
```

Move into the project directory:

```bash
cd AI-Sentiment-Analysis-Dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🔄 System Workflow

```text
Customer Feedback
       ↓
Text Processing
       ↓
Natural Language Processing
       ↓
Sentiment Polarity Analysis
       ↓
Positive / Negative / Neutral
```

---

## 📤 CSV Analysis

Users can upload a CSV file containing customer reviews or text data.

The dashboard allows the user to select the column containing text and automatically generates:

```text
Sentiment
Polarity
```

---

## 💡 Real-World Applications

Sentiment analysis can be used for:

- Customer feedback analysis
- Product review analysis
- Social media monitoring
- Brand reputation analysis
- Customer satisfaction analysis
- Survey response analysis
- Market research

---

## 🔮 Future Improvements

- BERT sentiment models
- Transformer-based NLP
- Emotion detection
- Aspect-based sentiment analysis
- Multilingual NLP
- Real-time social media analysis
- Automated sentiment reports

---

## 👩‍💻 Author

Developed as part of an Artificial Intelligence, Machine Learning and Data Analytics portfolio.
