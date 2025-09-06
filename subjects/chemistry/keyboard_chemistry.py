from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

chemistry_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Свойства химического элемента', callback_data='chemical_element'),
    ],
    [
        InlineKeyboardButton(text='Периодическая таблица', callback_data='periodic_table'),
    ],
    [
        InlineKeyboardButton(text='Таблица растворимости', callback_data='solubility_table'),
    ]
])

back_chemistry_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Назад 🔙', callback_data='back_chemistry')
    ]], resize_keyboard=True)
