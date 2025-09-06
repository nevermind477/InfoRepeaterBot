from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery, FSInputFile
from subjects.physics.keyboard_physics import physic_kb, back_physic_kb

router = Router()


@router.message(F.text == 'Физика 🎓')
async def physic1(message: Message):
    await message.answer('Выберите пункт', reply_markup=physic_kb)


@router.callback_query(F.data == 'back_physic')
async def chemistry2(callback: CallbackQuery):
    await callback.message.edit_text('Выберите пункт', reply_markup=physic_kb)


@router.callback_query(F.data == 'mechanics')
async def chemistry5(callback: CallbackQuery):
    await callback.message.ans(tetx='Периодическая таблица',
                               photo=FSInputFile('subjects/chemistry/periodic_table.png'))


@router.callback_query(F.data == 'electricity')
async def chemistry6(callback: CallbackQuery):
    await callback.message.answer_photo(text='Таблица растворимости',
                                        photo=FSInputFile('subjects/chemistry/solubility_table.png'))


@router.callback_query(F.data == 'optics')
async def chemistry6(callback: CallbackQuery):
    await callback.message.answer_photo(text='Таблица растворимости',
                                        photo=FSInputFile('subjects/chemistry/solubility_table.png'))
