from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hcode

from bot.design.commands import show_help, show_main_menu
from bot.design.keyboards import get_sticker_menu, CallbackData
from bot.helpers.msg_id import process_message
from bot.helpers.utils import extract_file_id, get_media_type

router = Router(name="main")


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.delete()
    await show_main_menu(message)


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.delete()
    await show_help(message)


@router.callback_query(F.data == CallbackData.HOW_TO_USE)
async def how_to_use_callback(callback: CallbackQuery):
    await show_help(callback)


@router.callback_query(F.data == CallbackData.BACK_TO_MAIN)
async def back_to_main_callback(callback: CallbackQuery):
    await show_main_menu(callback.message, edit=True)


@router.message(F.content_type.in_({'sticker', 'animation', 'document', 'photo'}))
async def handle_media(message: Message):
    file_id = extract_file_id(message)
    media_type = get_media_type(message)

    if not file_id or not media_type:
        await message.reply("Unable to get ID")
        return

    response = (
        f"Your user ID: {hcode(message.from_user.id)}\n"
        f"{media_type} ID: {hcode(file_id)}"
    )

    markup = None
    if media_type == "Sticker" and message.sticker and message.sticker.set_name:
        sticker_set_url = f"https://t.me/addstickers/{message.sticker.set_name}"
        markup = get_sticker_menu(sticker_set_url)

    await message.reply(response, reply_markup=markup)


@router.message(F.text)
async def handle_text(message: Message):
    await process_message(message)


@router.message(F.forward_date)
async def handle_forwards(message: Message):
    await process_message(message)
