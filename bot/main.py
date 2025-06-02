import asyncio



from Config.config import bd, bot
from bot.main_kb.main_kb import start_router


async def main():
    bd.include_router(start_router)
    await bd.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())