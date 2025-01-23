import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.handlers import router

BOT_TOKEN = ''


async def main():
    logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    dispatcher_logger = logging.getLogger('aiogram.dispatcher')
    dispatcher_logger.setLevel(logging.INFO)

    default = DefaultBotProperties(
        parse_mode=ParseMode.HTML,
        link_preview_is_disabled=True
    )
    bot = Bot(token=BOT_TOKEN, default=default)
    dp = Dispatcher()

    dp.include_router(router)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
