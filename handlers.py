from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from keyboards import main_keyboard, subject_keyboard

# Инициализация маршрутизатора для обработки сообщений
router = Router()


@router.message(CommandStart())
@router.message(F.text == 'В главное меню')
async def start(message: Message):
    """Обработчик команды /start и кнопки 'В главное меню'."""
    await message.answer_photo(
        photo=FSInputFile('data/logo.png'),  # Загружаем изображение логотипа
        caption='Привет! Я бот Inforepeater. Готов помочь тебе в изучении школьных тем! 📚',
        reply_markup=main_keyboard  # Отправляем главное меню
    )


@router.message(F.text == 'Выбрать предмет 📚')
async def choose_subject(message: Message):
    """Обработчик кнопки 'Выбрать предмет'."""
    await message.answer('Выберите пункт', reply_markup=subject_keyboard)  # Отправляем меню выбора предметов


@router.message(F.text == 'О боте ⁉️')
async def about_bot(message: Message):
    """Обработчик кнопки 'О боте'."""
    await message.answer(
        'Inforepeater — это твой умный учебный помощник, который помогает повторять и изучать школьные темы! 📚📝'
    )
