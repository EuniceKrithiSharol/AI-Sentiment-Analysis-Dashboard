from textblob import TextBlob


def analyze_text_sentiment(text):

    analysis = TextBlob(
        str(text)
    )


    polarity = analysis.sentiment.polarity


    if polarity > 0.15:

        sentiment = "Positive"

    elif polarity < -0.15:

        sentiment = "Negative"

    else:

        sentiment = "Neutral"


    return {

        "Sentiment": sentiment,

        "Polarity": polarity
    }


def analyze_multiple_texts(texts):

    results = []


    for text in texts:

        result = analyze_text_sentiment(
            text
        )


        results.append({

            "Text": text,

            "Sentiment": result[
                "Sentiment"
            ],

            "Polarity": result[
                "Polarity"
            ]
        })


    return results
