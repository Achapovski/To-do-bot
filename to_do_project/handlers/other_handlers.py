from aiogram.types import Message, CallbackQuery
from aiogram import Router

router = Router()


@router.message()
async def process_echo_answer(message: Message):
    await message.answer(message.text)


@router.callback_query()
async def process_echo_callback(callback: CallbackQuery):
    await callback.answer(callback.data)

