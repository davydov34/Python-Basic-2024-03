"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from models import engine, Base, User, Post, Session
from jsonplaceholder_requests import get_users, get_posts
from sqlalchemy.ext.asyncio import AsyncSession

async def add_users(session: AsyncSession, data: list[dict]):
    new_users = [User(id=u["id"], name=u["name"], username=u["username"], email=u["email"]) for u in data]
    session.add_all(new_users)
    await session.commit()

async def add_posts(session: AsyncSession, data: list[dict]):
    new_posts = [Post(id=p["id"], title=p["title"], body=p["body"], user_id=p["userId"]) for p in data]
    session.add_all(new_posts)
    await session.commit()

async def async_main():
    users_data: list[dict]
    posts_data: list[dict]

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    users_data, posts_data = await asyncio.gather(get_users(), get_posts())
    await asyncio.gather(add_users(Session(), users_data), add_posts(Session(), posts_data))


def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()