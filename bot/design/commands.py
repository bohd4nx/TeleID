from enum import Enum

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hbold, hlink, hcode

from bot.design.keyboards import get_main_menu, get_help_menu

command_router = Router(name="commands")


class Commands(str, Enum):
    START = "start"
    HELP = "help"


@command_router.message(Command(Commands.START))
async def start_command(message: Message):
    await message.delete()
    await show_main_menu(message)


async def show_main_menu(message: Message, edit: bool = False):
    caption = (
        f"{hbold('👋 Welcome!')}\n\n"
        "🤖 I'll help you get the ID of any media file in Telegram:\n"
        "• Stickers (including animated)\n"
        "• GIF animations\n"
        "• Documents\n"
        "• Photos\n\n"
        f"📚 Source: {hlink('GitHub Repository', 'https://github.com/bohd4nx/TeleID')}"
    )

    if edit:
        await message.edit_text(text=caption, reply_markup=get_main_menu())
    else:
        await message.answer(text=caption, reply_markup=get_main_menu())


@command_router.message(Command(Commands.HELP))
async def help_command(message: Message):
    await message.delete()
    await show_help(message)


async def show_help(message_or_query):
    caption = (
        f"{hbold('📖 How to use:')}\n\n"
        "1️⃣ Send me any media file:\n"
        "   • Sticker or animated sticker\n"
        "   • GIF animation\n"
        "   • Document\n"
        "   • Photo\n"
        f"2️⃣ I'll reply with the file's {hcode('ID')}\n"
        "3️⃣ For stickers, you'll get a link to the sticker pack\n"
    )

    if isinstance(message_or_query, CallbackQuery):
        await message_or_query.message.edit_text(
            text=caption,
            reply_markup=get_help_menu()
        )
    else:
        await message_or_query.answer(
            text=caption,
            reply_markup=get_help_menu()
        )
