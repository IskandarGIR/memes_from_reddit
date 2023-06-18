import asyncio
import os
import asyncpraw
from aiogram import Bot, types
from dotenv import load_dotenv
load_dotenv()

CHANNEL_ID = os.getenv('CHANNEL_ID')

bot = Bot(token=os.getenv('API_TOKEN'), parse_mode=types.ParseMode.HTML)
reddit = asyncpraw.Reddit(client_id=os.getenv('CLIENT_ID'),
                          client_secret=os.getenv('SECRETE_CODE'),
                          user_agent='random_reddit_bot/0.0.1')

memes = []
TIMEOUT = 5
SUBREDDIT_NAME = 'memes'
POST_LIMIT = 1


async def send_mem(channel_id: int, title: str, photo_url: str):
    await bot.send_photo(channel_id, photo=photo_url, caption=title)


async def main():
    while True:
        await asyncio.sleep(TIMEOUT)
        memes_submissions = await reddit.subreddit(SUBREDDIT_NAME)
        memes_submissions = memes_submissions.new(limit=POST_LIMIT)
        for _ in range(POST_LIMIT):
            global memes
            mem = await memes_submissions.__anext__()
            if mem.title not in memes:
                memes.append(mem.title)
                await send_mem(CHANNEL_ID, mem.title, mem.url)
        if len(memes) > 10:
            memes = memes[9:]


loop = asyncio.get_event_loop()
loop.run_until_complete(main())