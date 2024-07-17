from aiogram.types import BotCommand
from aiogram import Bot


async def set_main_menu(bot: Bot):
    main_menu = [
        BotCommand(
            command="/start",
            description="Start bot."
        ),
        BotCommand(
            command="/help",
            description="What can i do."
        ),
        BotCommand(
            command="/info",
            description="Information about me and my creator."
        ),
        BotCommand(
            command="/add_task",
            description="Add task to queue"
        ),
        BotCommand(
            command="/show_tasks",
            description="Show queue of tasks",
        ),
    ]
    await bot.set_my_commands(main_menu)




