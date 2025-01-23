from aiogram import types


def extract_file_id(content: types.Message) -> str:
    if content.sticker:
        return content.sticker.file_id
    elif content.animation:
        return content.animation.file_id
    elif content.document:
        return content.document.file_id
    elif content.photo:
        return content.photo[-1].file_id
    return None


def get_media_type(message: types.Message) -> str:
    if message.sticker:
        return "Sticker"
    elif message.animation:
        return "GIF"
    elif message.document:
        return "Document"
    elif message.photo:
        return "Photo"
    return None
