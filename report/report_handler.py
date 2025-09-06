from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from report.report_GoogleSheet import bag_report
from report.report_keyboard import report_sheet

# Инициализация маршрутизатора
router = Router()


# Определение состояний для FSM (Finite State Machine)
class UserStates(StatesGroup):
    waiting_for_input = State()  # Ожидание ввода от пользователя


# Обработчик для сообщения об ошибках или предложениях
@router.message(F.text == 'Сообщить об ошибке/Предложить идею 💬')
async def report_error(message: Message, state: FSMContext):
    """Запрашивает у пользователя описание проблемы и устанавливает состояние ожидания ввода."""
    await message.answer('Опишите проблему')  # Запрос на ввод
    await state.set_state(UserStates.waiting_for_input)  # Установка состояния ожидания ввода


# Обработчик для обработки отчета об ошибке
@router.message(UserStates.waiting_for_input)
async def handle_error_report(message: Message, state: FSMContext):
    """Обрабатывает текст сообщения от пользователя и сохраняет его в Google Sheets."""
    user_input = message.text  # Получение текста от пользователя
    await message.answer(
        'Спасибо за обращение, мы обязательно постараемся решить вашу проблему')  # Подтверждение получения
    await message.answer('Вы можете ознакомиться со списком актуальных проблем',
                         reply_markup=report_sheet)  # Предложение посмотреть список проблем

    # Запись отчета в Google Sheets
    bag_report('BagReport', 1, user_input)  # Логирование отчета

    await state.clear()  # Очистка состояния после обработки
