from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

from subjects.informatics.keyboard_informatic import informatics_kb, cc_calculator_kb
from subjects.informatics.cc_calculator import convert_number

router = Router()


@router.message(F.text == 'Информатика 👨‍💻')
async def informatics(message: Message):
    await message.answer('Выберите предмет', reply_markup=informatics_kb)


@router.callback_query(F.data == 'back_inform')
async def back_inform(callback: CallbackQuery):
    await callback.message.edit_text('Выберите предмет', reply_markup=informatics_kb)


class Reg(StatesGroup):
    number = State()
    from_base = State()
    to_base = State()


@router.callback_query(F.data == 'cc_calculator')
async def start_conversion(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Введите число')
    await state.set_state(Reg.number)


@router.message(Reg.number)
async def reg_number(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(Reg.from_base)
    await message.answer('Введите основание числа (2-36):')


@router.message(Reg.from_base)
async def reg_from_base(message: Message, state: FSMContext):
    await state.update_data(from_base=message.text)
    await state.set_state(Reg.to_base)
    await message.answer('Введите целевую систему счисления (2-36):')


@router.message(Reg.to_base)
async def reg_to_base(message: Message, state: FSMContext):
    await state.update_data(to_base=message.text)
    cc = await state.get_data()
    await state.clear()
    result = convert_number(cc['number'], int(cc['from_base']), int(cc['to_base']))
    await message.answer(text=result)
