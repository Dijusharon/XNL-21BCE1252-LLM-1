# backend/app/market_data/data_ingestion.py
import requests
import json

def fetch_crypto_data():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data = response.json()
    return data

def fetch_stock_data():
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": "AAPL",
        "interval": "5min",
        "apikey": "YOUR_API_KEY"
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    print(fetch_crypto_data())
    print(fetch_stock_data())
