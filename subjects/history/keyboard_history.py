from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

history_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='История России', callback_data='date')
    ]])

back_history_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Назад 🔙', callback_data='back_history')
    ]], resize_keyboard=True)
