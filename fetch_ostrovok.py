from base64 import b64encode

import requests
import os

from dotenv import load_dotenv

from database import save_hotels_to_db

load_dotenv()

OSTROVOK_API_URL = "https://api.worldota.net/api/b2b/v3/search/serp/region/"

async def fetch_ostrovok_hotels():
    cities = [1913, 1361, 2427, 481, 1639, 1178]
    hotels = []
    auth_header = b64encode(os.getenv('OSTROVOK_API_KEY').encode('utf-8')).decode("ascii")
    headers = {
        'Authorization': f"Basic {auth_header}"
    }
    for city_id in cities:
        params = {
            # 'region_id': city_id,
            # 'limit': 20
        }
        response = requests.get(OSTROVOK_API_URL, headers=headers, params=params)
        print(response)
        if response.status_code == 200:
            data = response.json()
            print(data)
            hotels.extend(data.get('hotels', []))
    await save_hotels_to_db(hotels, 'ostrovok')
    return hotels
