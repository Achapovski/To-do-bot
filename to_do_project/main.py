from aiogram import Bot, Dispatcher, F
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from config_data.config import load_config_settings, Config
from handlers import user_handlers, other_handlers
from keyboards.main_menu import set_main_menu

import asyncio


async def main():

    # Инициализирую конфиг
    config: Config = load_config_settings()

    # Инициализирую бота и диспетчер
    bot = Bot(
        token=config.bot.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    # Подключаю роутеры к диспетчеру
    dp.include_router(router=user_handlers.router)
    dp.include_router(router=other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await set_main_menu(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

