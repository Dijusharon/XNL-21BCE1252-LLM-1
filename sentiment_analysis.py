# backend/app/sentiment_analysis/sentiment.py
from transformers import pipeline

nlp = pipeline("sentiment-analysis")

def analyze_market_sentiment(text):
    result = nlp(text)
    return result

if __name__ == "__main__":
    sample_news = "Bitcoin surges 10% as institutional investors pour in capital!"
    print(analyze_market_sentiment(sample_news))
