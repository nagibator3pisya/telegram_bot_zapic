import asyncio

from Config.config import bd, bot
from bot.kb_commant_user.hendler_user import handled_user_router
from bot.kb_commant_user.kb_user import user_router
from bot.main_kb.hendler_main import hendler_router_main
# from bot.km_command_admin.hendler_admin import admin_router
from bot.main_kb.start_ import start_router


async def main():
    bd.include_router(start_router)
    bd.include_router(user_router)
    bd.include_router(handled_user_router)
    bd.include_router(hendler_router_main)
    # bd.include_router(admin_router)
    await bd.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())