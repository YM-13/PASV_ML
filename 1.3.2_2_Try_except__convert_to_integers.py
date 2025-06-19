"""Конвертация типов

Напишите функцию, которая принимает список строк и конвертирует его в список целых чисел. Обработайте исключения,
возникающие при невозможности конвертации строки в число."""

def convert_to_integers(string_list):
    # ваш код здесь
    int_list = []
    for string in string_list:
        try:
            res = int(string)
            int_list.append(res)
        except ValueError:
            print(f'"{string}" is not the number. Incorrect type of data')

    return int_list
# Тестовый пример
print(convert_to_integers(["1", "2", "три"]))  # Ожидаемый вывод: [1, 2] и сообщение об ошибке
