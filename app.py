import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from textblob import TextBlob


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="AI Sentiment Analysis Dashboard",
    page_icon="😊",
    layout="wide"
)


# -------------------------------------------------
# SENTIMENT ANALYSIS FUNCTION
# -------------------------------------------------

def analyze_sentiment(text):

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity


    if polarity > 0.15:

        sentiment = "Positive"

    elif polarity < -0.15:

        sentiment = "Negative"

    else:

        sentiment = "Neutral"


    return sentiment, polarity


# -------------------------------------------------
# SAMPLE DATASET
# -------------------------------------------------

@st.cache_data
def create_sample_data():

    reviews = [

        "The product is amazing and works perfectly.",

        "Excellent quality and very fast delivery.",

        "I absolutely love this product.",

        "The service was terrible and disappointing.",

        "Very poor quality. I will not buy again.",

        "The product stopped working after one week.",

        "The product is okay and works as expected.",

        "Average experience. Nothing special.",

        "The quality is acceptable for the price.",

        "Fantastic customer support and great service.",

        "I am very happy with my purchase.",

        "The delivery was late and the product was damaged.",

        "Not bad, but it could be improved.",

        "Amazing experience. Highly recommended.",

        "I am disappointed with the product quality.",

        "The application is easy to use and very helpful.",

        "The user interface is confusing.",

        "Good product but the delivery took too long.",

        "Excellent performance and great value for money.",

        "The product does not meet my expectations."
    ]


    data = pd.DataFrame({

        "Review": reviews
    })


    results = data["Review"].apply(
        analyze_sentiment
    )


    data["Sentiment"] = [

        result[0]

        for result in results
    ]


    data["Polarity"] = [

        result[1]

        for result in results
    ]


    return data


sentiment_data = create_sample_data()


# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title(
    "😊 AI Sentiment Analysis Dashboard"
)


st.markdown(
    "Analyze customer feedback and text using Natural "
    "Language Processing to identify positive, negative, "
    "and neutral sentiment."
)


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.header(
    "🧠 How It Works"
)


st.sidebar.info(
    """
    1. Text is entered or uploaded.

    2. NLP analyzes the text.

    3. Sentiment polarity is calculated.

    4. The text is classified as Positive, Negative, or Neutral.

    5. Analytics and visualizations are generated.
    """
)


# -------------------------------------------------
# METRICS
# -------------------------------------------------

st.subheader(
    "📊 Sentiment Overview"
)


total_reviews = len(
    sentiment_data
)


positive_reviews = len(

    sentiment_data[
        sentiment_data[
            "Sentiment"
        ] == "Positive"
    ]
)


negative_reviews = len(

    sentiment_data[
        sentiment_data[
            "Sentiment"
        ] == "Negative"
    ]
)


neutral_reviews = len(

    sentiment_data[
        sentiment_data[
            "Sentiment"
        ] == "Neutral"
    ]
)


col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Reviews",
    total_reviews
)


col2.metric(
    "Positive",
    positive_reviews
)


col3.metric(
    "Negative",
    negative_reviews
)


col4.metric(
    "Neutral",
    neutral_reviews
)


# -------------------------------------------------
# DATASET PREVIEW
# -------------------------------------------------

st.subheader(
    "📁 Customer Feedback Dataset"
)


st.dataframe(
    sentiment_data,
    use_container_width=True
)


# -------------------------------------------------
# SENTIMENT DISTRIBUTION
# -------------------------------------------------

st.subheader(
    "📊 Sentiment Distribution"
)


sentiment_counts = (

    sentiment_data[
        "Sentiment"
    ]
    .value_counts()
    .reset_index()
)


sentiment_counts.columns = [

    "Sentiment",

    "Count"
]


fig_sentiment = px.pie(

    sentiment_counts,

    names="Sentiment",

    values="Count",

    title="Customer Sentiment Distribution"
)


st.plotly_chart(
    fig_sentiment,
    use_container_width=True
)


# -------------------------------------------------
# POLARITY DISTRIBUTION
# -------------------------------------------------

st.subheader(
    "📈 Sentiment Polarity Analysis"
)


fig_polarity = px.histogram(

    sentiment_data,

    x="Polarity",

    color="Sentiment",

    nbins=20,

    title="Sentiment Polarity Distribution"
)


st.plotly_chart(
    fig_polarity,
    use_container_width=True
)


# -------------------------------------------------
# INDIVIDUAL TEXT ANALYSIS
# -------------------------------------------------

st.divider()


st.header(
    "🔍 Analyze Text Sentiment"
)


user_text = st.text_area(

    "Enter text to analyze",

    placeholder="Type a customer review, comment, or feedback here..."
)


if st.button(
    "🤖 Analyze Sentiment"
):

    if user_text.strip() == "":

        st.warning(
            "Please enter some text before analyzing."
        )

    else:

        sentiment, polarity = analyze_sentiment(
            user_text
        )


        st.divider()


        st.subheader(
            "AI Sentiment Analysis Result"
        )


        col1, col2 = st.columns(2)


        col1.metric(
            "Sentiment",
            sentiment
        )


        col2.metric(
            "Polarity Score",
            round(
                polarity,
                3
            )
        )


        if sentiment == "Positive":

            st.success(
                "😊 Positive Sentiment Detected"
            )


        elif sentiment == "Negative":

            st.error(
                "😞 Negative Sentiment Detected"
            )


        else:

            st.info(
                "😐 Neutral Sentiment Detected"
            )


# -------------------------------------------------
# CSV UPLOAD
# -------------------------------------------------

st.divider()


st.header(
    "📤 Analyze Customer Feedback CSV"
)


uploaded_file = st.file_uploader(

    "Upload a CSV file containing text",

    type=["csv"]
)


if uploaded_file is not None:

    uploaded_data = pd.read_csv(
        uploaded_file
    )


    st.subheader(
        "Uploaded Data Preview"
    )


    st.dataframe(
        uploaded_data.head(),
        use_container_width=True
    )


    text_column = st.selectbox(

        "Select the text column",

        uploaded_data.columns
    )


    if st.button(
        "Analyze Uploaded Feedback"
    ):

        uploaded_data = uploaded_data.dropna(

            subset=[
                text_column
            ]
        )


        uploaded_data["Sentiment"] = uploaded_data[
            text_column
        ].apply(
            lambda x: analyze_sentiment(
                str(x)
            )[0]
        )


        uploaded_data["Polarity"] = uploaded_data[
            text_column
        ].apply(
            lambda x: analyze_sentiment(
                str(x)
            )[1]
        )


        st.subheader(
            "Sentiment Analysis Results"
        )


        st.dataframe(
            uploaded_data,
            use_container_width=True
        )


        uploaded_counts = (

            uploaded_data[
                "Sentiment"
            ]
            .value_counts()
            .reset_index()
        )


        uploaded_counts.columns = [

            "Sentiment",

            "Count"
        ]


        fig_uploaded = px.bar(

            uploaded_counts,

            x="Sentiment",

            y="Count",

            title="Uploaded Feedback Sentiment Analysis"
        )


        st.plotly_chart(
            fig_uploaded,
            use_container_width=True
        )


# -------------------------------------------------
# SAMPLE REVIEW EXPLORER
# -------------------------------------------------

st.divider()


st.header(
    "📊 Explore Sample Feedback"
)


selected_sentiment = st.selectbox(

    "Filter by sentiment",

    [

        "All",

        "Positive",

        "Negative",

        "Neutral"
    ]
)


if selected_sentiment == "All":

    filtered_data = sentiment_data

else:

    filtered_data = sentiment_data[

        sentiment_data[
            "Sentiment"
        ] == selected_sentiment

    ]


st.dataframe(
    filtered_data,
    use_container_width=True
)


# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.divider()


st.caption(
    "AI Sentiment Analysis Dashboard | "
    "Python • NLP • Text Analysis • "
    "Sentiment Analysis • Streamlit"
)
