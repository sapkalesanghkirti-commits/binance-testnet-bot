import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    client = Client(api_key, api_secret, testnet=True)

    # Force server time sync
    client.futures_ping()  # this makes a request, syncs server
    server_time = client.futures_time()
    client.timestamp_offset = server_time['serverTime'] - int(client.get_server_time()['serverTime'])

    return client