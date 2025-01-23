from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.design.commands import show_help, show_main_menu
from bot.design.keyboards import CallbackData


class BaseHandler:
    def __init__(self):
        self.router = Router(name=self.__class__.__name__)

    async def handle(self, *args, **kwargs):
        raise NotImplementedError


class CallbackHandler(BaseHandler):
    def get_router(self) -> Router:
        return self.router


class MenuCallbacks(CallbackHandler):
    def __init__(self):
        super().__init__()
        self.router.callback_query.register(self.how_to_use, F.data == CallbackData.HOW_TO_USE)
        self.router.callback_query.register(self.back_to_main, F.data == CallbackData.BACK_TO_MAIN)

    @staticmethod
    async def how_to_use(callback: CallbackQuery):
        await show_help(callback)

    @staticmethod
    async def back_to_main(callback: CallbackQuery):
        await show_main_menu(callback.message, edit=True)
