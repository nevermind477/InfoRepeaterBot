from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

# Определение клавиатура для информатики
informatics_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Перевод сс', callback_data='cc_calculator'),
    ],
    [
        InlineKeyboardButton(text='Ссылка на SDO', url='https://sdo24.1580.ru')
    ]
], resize_keyboard=True)

# Определение клавиатуры для калькулятора
cc_calculator_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Перевод', callback_data='perevod')
    ],
    [
        InlineKeyboardButton(text='Назад', callback_data='back_inform')
    ]
], resize_keyboard=True)
