from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

from subjects.russian.keyboard_russian import russian_kb, back_russian_kb
from subjects.russian.vocabulary_words import vocabulary_words

router = Router()


class RussianStates(StatesGroup):
    number = State()
    letter = State()


@router.message(F.text == 'Русский язык 📝')
async def handle_russian_language_selection(message: Message):
    await message.answer('Выберите пункт', reply_markup=russian_kb)


@router.callback_query(F.data == 'back_russian')
async def handle_back_russian(callback: CallbackQuery):
    await callback.message.edit_text('Выберите пункт', reply_markup=russian_kb)


@router.callback_query(F.data == 'vocabulary_words')
async def handle_vocabulary_words_selection(callback: CallbackQuery, state: FSMContext):
    await state.set_state(RussianStates.number)
    await callback.message.edit_text('Введите класс, за который хотите получить словарные слова',
                                     reply_markup=back_russian_kb)


@router.message(RussianStates.number)
async def handle_class_number_input(message: Message, state: FSMContext):
    input_number = message.text
    # Вы можете добавить валидацию для input_number здесь
    await state.update_data(class_number=input_number)  # Сохраняем номер класса
    await state.set_state(RussianStates.letter)
    await message.answer('Введите букву, на которую начинаются словарные слова')


@router.message(RussianStates.letter)
async def handle_letter_input(message: Message, state: FSMContext):
    input_data = await state.get_data()  # Получаем сохраненные данные
    input_number = input_data.get('class_number')
    input_letter = message.text
    words = await vocabulary_words(input_number, input_letter)
    await message.answer(text=words)
    await state.clear()
