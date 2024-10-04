import logging
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def func_alert(hotel, competitor_price):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")  # Bot token from .env
    chat_id = os.getenv("TELEGRAM_CHAT_ID")  # Chat ID from .env

    message = f"Hotel {hotel['name']} has a non-competitive price! Competitor price: {competitor_price}."

    # Sending message to Telegram
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        logging.info("Alert sent successfully!")
    else:
        logging.info(f"Failed to send alert: {response.status_code} - {response.text}")

async def analyze_prices(ostrovok_hotels, hotellook_hotels):

    hotellook_prices = {hotel['id']: hotel['price'] for hotel in hotellook_hotels}


    analysis_requests = []

    for ostrovok_hotel in ostrovok_hotels:
        hotel_id = ostrovok_hotel['id']
        ostrovok_price = ostrovok_hotel['price']
        competitor_price = hotellook_prices.get(hotel_id)


        if competitor_price:
            analysis_requests.append({
                'name': ostrovok_hotel['name'],
                'ostrovok_price': ostrovok_price,
                'competitor_price': competitor_price
            })


    if analysis_requests:
        for request in analysis_requests:
            prompt = (
                f"Analyze the pricing for the hotel '{request['name']}'. "
                f"Ostrovok price: {request['ostrovok_price']}, "
                f"Competitor price: {request['competitor_price']}. "
                "Is the Ostrovok price competitive? If not, suggest a competitive price."
            )

            response = await get_chatgpt_analysis(prompt)


            if response.get("is_competitive") is False:
                func_alert(ostrovok_hotel, request['competitor_price'])


async def get_chatgpt_analysis(prompt):
    api_key = os.getenv("")
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 100,
        "temperature": 0.5
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        chat_response = response.json()

        response_content = chat_response['choices'][0]['message']['content']


        is_competitive = "not competitive" in response_content.lower()

        return {
            "response": response_content,
            "is_competitive": not is_competitive
        }
    else:
        logging.info(f"Error from OpenAI API: {response.status_code} - {response.text}")
        return {"is_competitive": True}
