# api.py

import requests
from config import API_URL, CURRENCIES

def get_current_prices():
    """Fetch current prices of selected cryptocurrencies."""
    url = f"{API_URL}/simple/price"
    params = {
        "ids": ",".join(CURRENCIES),
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    return response.json()

def get_historical_data(crypto_id, days=30):
    """Fetch historical data for a specific cryptocurrency."""
    url = f"{API_URL}/coins/{crypto_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days
    }
    response = requests.get(url, params=params)
    return response.json()
