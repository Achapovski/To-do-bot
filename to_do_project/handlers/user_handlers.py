from aiogram import F
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from lexicon.lexicon import LEXICON_RU, LEXICON_COMMANDS
from keyboards.keyboards import load_keyboard

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer("I`m here")


@router.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(LEXICON_COMMANDS["/help"])


@router.message(Command(commands="info"))
async def process_info_command(message: Message):
    await message.answer(LEXICON_COMMANDS["/info"])


@router.message(Command(commands="add_task"))
async def process_add_task_command(message: Message):
    await message.answer(
        text="What do you want to do ?",
        reply_markup=load_keyboard("add", "edit", "delete", test_button="Yoohhooo", adjust=(3, 1))
    )
