import asyncio



from Config.config import bd, bot


async def main():
    await bd.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())