from aiogram import types
from aiogram.utils.markdown import hcode


def format_user_info(user_or_chat) -> str:
    entity_id = user_or_chat.id
    username = f"@{user_or_chat.username}" if user_or_chat.username else "None"
    return f"{hcode(entity_id)} | {username}"


async def process_message(message: types.Message):
    response = (
        f"Your user ID: {hcode(message.from_user.id)}\n"
        f"Current chat ID: {hcode(message.chat.id)}"
    )

    if forward_source := message.forward_from or message.forward_from_chat:
        response += f"\nForwarded from: {format_user_info(forward_source)}"

    await message.reply(response)
