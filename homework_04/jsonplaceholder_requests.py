"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
from datetime import datetime

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch_json(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        content = await response.json()
        return content

async def get_users():
    content = await fetch_json(USERS_DATA_URL)
    return content

async def get_posts():
    content = await fetch_json(POSTS_DATA_URL)
    return content

