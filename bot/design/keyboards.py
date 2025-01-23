from enum import Enum

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class CallbackData(str, Enum):
    HOW_TO_USE = "how_to_use"
    BACK_TO_MAIN = "back_to_main"


def get_main_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="ℹ️ How to use", callback_data=CallbackData.HOW_TO_USE)
    )
    return builder.as_markup()


def get_help_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="« Back", callback_data=CallbackData.BACK_TO_MAIN)
    )
    return builder.as_markup()


def get_sticker_menu(sticker_set_url: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="➕ Add Stickers", url=sticker_set_url)
    )
    return builder.as_markup()
