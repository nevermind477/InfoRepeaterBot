def convert_number(number: str, from_base: int, to_base: int) -> str:
    """
    Переводит число из одной системы счисления в другую.

    :param number: Исходное число в виде строки.
    :param from_base: Система счисления исходного числа (от 2 до 36).
    :param to_base: Система счисления, в которую нужно перевести число (от 2 до 36).
    :return: Число в виде строки в новой системе счисления.
    """
    # Преобразуем число из исходной системы счисления в десятичную
    decimal_number = int(number, from_base)

    # Если целевая система счисления - 10, просто возвращаем число
    if to_base == 10:
        return str(decimal_number)

    # Переводим число из десятичной системы в целевую
    if to_base < 2 or to_base > 36:
        raise ValueError("Целевая система счисления должна быть от 2 до 36.")

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while decimal_number > 0:
        result = digits[decimal_number % to_base] + result
        decimal_number //= to_base

    return result if result else "0"


# Пример использования
'''if __name__ == "__main__":
    number = "1010"  # Исходное число
    from_base = 7  # Исходная система счисления
    to_base = 15  # Целевая система счисления

    converted_number = convert_number(number, from_base, to_base)
    print(f"{number} из системы счисления {from_base} в систему счисления {to_base} равно {converted_number}")'''
