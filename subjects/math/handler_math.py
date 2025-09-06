from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery, FSInputFile

router = Router()


@router.message(F.text == 'Математика 🧮')
async def history1(message: Message):
    await message.answer('Здесь пока ничего нет 🥲')
