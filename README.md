# Hotel Price Analysis System

This project periodically fetches hotel data from two APIs (Ostrovok and Hotel Look), stores the data in a MongoDB database, analyzes prices using ChatGPT, and alerts if the prices are not competitive.

## Features

- Fetches hotel data for specific cities from the Ostrovok and Hotel Look APIs.
- Stores hotel data in two separate MongoDB collections.
- Analyzes pricing using ChatGPT to determine competitiveness.
- Sends alerts via Telegram bot if prices are found to be non-competitive.


## Installation

### Prerequisites

- Python 3.9 or higher
- MongoDB (local or cloud instance)
- A Telegram bot for sending alerts


### Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies

Install the required Python packages using pip:
```pip install -r requirements.txt```

### Setup environment variables
```bash
OSTROVOK_API_KEY=your_ostrovok_api_key
HOTELLOOK_API_KEY=your_hotellook_api_key
OPENAI_API_KEY=your_openai_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
MONGODB_URI=mongodb://localhost:27017/yourdbname
```

To start the application, run:
```python main.py```


