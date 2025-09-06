from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery, FSInputFile
from subjects.chemistry.keyboard_chemistry import chemistry_kb, back_chemistry_kb
from subjects.chemistry.chemical_element import display_element_info

router = Router()


class chemistry(StatesGroup):
    chemical_element = State()


@router.message(F.text == 'Химия 🧪')
async def chemistry1(message: Message):
    await message.answer('Выберите пункт', reply_markup=chemistry_kb)


@router.callback_query(F.data == 'back_chemistry')
async def chemistry2(callback: CallbackQuery):
    await callback.message.edit_text('Выберите пункт', reply_markup=chemistry_kb)


@router.callback_query(F.data == 'chemical_element')
async def chemistry3(callback: CallbackQuery, state: FSMContext):
    await state.set_state(chemistry.chemical_element)
    await callback.message.edit_text('Введите символьное обозначение химического элемента',
                                     reply_markup=back_chemistry_kb)


@router.message(chemistry.chemical_element)
async def chemistry4(message: Message, state: FSMContext):
    user_input = message.text
    await display_element_info(user_input, message)
    await state.clear()


@router.callback_query(F.data == 'periodic_table')
async def chemistry5(callback: CallbackQuery):
    await callback.message.answer_photo(tetx='Периодическая таблица',
                                        photo=FSInputFile('subjects/chemistry/periodic_table.png'))


@router.callback_query(F.data == 'solubility_table')
async def chemistry6(callback: CallbackQuery):
    await callback.message.answer_photo(text='Таблица растворимости',
                                        photo=FSInputFile('subjects/chemistry/solubility_table.png'))
