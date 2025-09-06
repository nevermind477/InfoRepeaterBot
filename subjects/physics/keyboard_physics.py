from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

physic_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Механика', callback_data='mechanics'),
        InlineKeyboardButton(text='Термодинамика', callback_data='thermodynamics'),
    ],
    [
        InlineKeyboardButton(text='Электричество', callback_data='electricity'),
        InlineKeyboardButton(text='Оптика', callback_data='optics'),
    ]
], resize_keyboard=True)

back_physic_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Назад 🔙', callback_data='back_physic')
    ]
], resize_keyboard=True)
