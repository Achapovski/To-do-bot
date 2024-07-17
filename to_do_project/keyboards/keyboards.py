from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder, KeyboardBuilder, InlineKeyboardMarkup
from keyboards.buttons import DEFAULT_BUTTONS


def load_keyboard(
        *buttons: str,
        width: int = 2,
        adjust: () = (),
        **named_buttons: [str, str]) -> InlineKeyboardMarkup:

    kb_builder = InlineKeyboardBuilder()

    kb_builder.row(*[
        InlineKeyboardButton(
            text=f"{DEFAULT_BUTTONS.get(button, button)}",
            callback_data=f"{button}",
        ) for button in buttons], width=width)

    kb_builder.row(*[
        InlineKeyboardButton(
            text=f"{title}",
            callback_data=f"{name}",
        ) for name, title in named_buttons.items()], width=width)

    kb_builder.adjust(*adjust) if adjust else ...

    return kb_builder.as_markup()


