# sentiment_analysis.py
# Sentiment Analysis using TextBlob
# Made by Shikha 😊

from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    print("\n--- Sentiment Report ---")
    print(f"Input Text      : {text}")
    print(f"Polarity        : {polarity:.2f}")
    print(f"Subjectivity    : {subjectivity:.2f}")

    # Interpretation
    if polarity > 0:
        print("Overall Sentiment: Positive 😊")
    elif polarity < 0:
        print("Overall Sentiment: Negative 😡")
    else:
        print("Overall Sentiment: Neutral 😐")


# -------- Main Program --------
if __name__ == "__main__":
    print("📌 Welcome to Sentiment Analysis Project 📌")
    print("Type 'exit' to quit.\n")

    while True:
        user_text = input("Enter a sentence: ")

        if user_text.lower() == "exit":
            print("Goodbye 👋")
            break

        analyze_sentiment(user_text)
