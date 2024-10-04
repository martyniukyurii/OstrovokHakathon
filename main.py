import aioschedule as schedule
import asyncio
from fetch_ostrovok import fetch_ostrovok_hotels
from fetch_hotellook import fetch_hotellook_hotels
from price_analysis import analyze_prices

async def job():
    ostrovok_hotels = await fetch_ostrovok_hotels()
    hotellook_hotels = await fetch_hotellook_hotels()
    await analyze_prices(ostrovok_hotels, hotellook_hotels)

async def scheduler():
    schedule.every(1).minutes.do(job)
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(scheduler())
