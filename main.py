import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def map_to_emoji(score):
    if score >= 0.5:
        return "😃"  # happy face emoji
    elif score <= -0.5:
        return "😔"  # sad face emoji
    else:
        return "😐"  # neutral face emoji

input_text = input("Enter some text: ")

polarity_scores = sia.polarity_scores(input_text)
sentiment_score = polarity_scores["compound"]
emoji = map_to_emoji(sentiment_score)

print(f"Sentiment score: {sentiment_score:.2f}")
print(f"Emoji: {emoji}")
