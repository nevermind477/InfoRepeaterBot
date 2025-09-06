import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import SCOPE, SHEET_ID, JSON


def bag_report(sheet_name, column, values_input):
    """
    Функция для добавления значений в указанный столбец Google Sheets.

    :param sheet_name: Название листа в таблице
    :param column: Номер столбца, в который будут добавлены значения
    :param values_input: Строка значений, разделенных запятыми
    """
    # Разделение входной строки на отдельные значения и удаление лишних пробелов
    values = [value.strip() for value in values_input.split(',')]

    # Аутентификация и авторизация с использованием учетных данных
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON, SCOPE)
    client = gspread.authorize(creds)

    # Открытие таблицы по ID и выбор рабочего листа
    sheet = client.open_by_key(SHEET_ID)
    worksheet = sheet.worksheet(sheet_name)

    # Получение текущих значений в указанном столбце
    col_values = worksheet.col_values(column)

    # Определение первой пустой строки в столбце
    first_empty_row = len(col_values) + 1

    # Определение диапазона ячеек для обновления
    cell_list = worksheet.range(
        f'{chr(64 + column)}{first_empty_row}:{chr(64 + column)}{first_empty_row + len(values) - 1}'
    )

    # Обновление значений в ячейках
    for i, cell in enumerate(cell_list):
        cell.value = values[i]

    # Запись обновленных значений обратно в таблицу
    worksheet.update_cells(cell_list)
