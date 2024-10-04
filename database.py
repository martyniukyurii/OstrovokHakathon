from motor.motor_asyncio import AsyncIOMotorClient
import os

client = AsyncIOMotorClient(os.getenv('MONGO_URI'))
db = client['hotel_database']

async def save_hotels_to_db(hotels, source):
    collection = db[f"{source}_hotels"]
    await collection.insert_many(hotels)

async def get_hotels_from_db(source):
    collection = db[f"{source}_hotels"]
    return await collection.find().to_list(length=None)
