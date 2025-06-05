import asyncio



from Config.config import bd, bot
from bot.kb_commant_user.kb_user import user_router
from bot.main_kb.start_ import start_router


async def main():
    bd.include_router(start_router)
    bd.include_router(user_router)
    await bd.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())