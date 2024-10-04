import requests
from database import save_hotels_to_db

HOTELLOOK_API_URL = "https://api.hotellook.com/api/v2/hotels"

async def fetch_hotellook_hotels():
    cities = [1913, 1361, 2427, 481, 1639, 1178]
    hotels = []
    for city_id in cities:
        params = {
            'region_id': city_id,
            'limit': 20
        }
        response = requests.get(HOTELLOOK_API_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            hotels.extend(data.get('hotels', []))
    await save_hotels_to_db(hotels, 'hotellook')
    return hotels
