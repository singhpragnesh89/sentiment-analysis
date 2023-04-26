import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# download necessary NLTK resources
nltk.download('vader_lexicon')

# create a sentiment analyzer object
sia = SentimentIntensityAnalyzer()

# define a function to map sentiment scores to emojis
def map_to_emoji(score):
    if score >= 0.5:
        return "😃"  # happy face emoji
    elif score <= -0.5:
        return "😔"  # sad face emoji
    else:
        return "😐"  # neutral face emoji

# take input from the user
input_text = input("Enter some text: ")

# analyze the sentiment of the input text and map to an emoji
polarity_scores = sia.polarity_scores(input_text)
sentiment_score = polarity_scores["compound"]
emoji = map_to_emoji(sentiment_score)

# print the sentiment score and emoji for the input text
print(f"Sentiment score: {sentiment_score:.2f}")
print(f"Emoji: {emoji}")
