"""Получение информации об ошибке

Напишите функцию, которая пытается преобразовать входную строку в число и, в случае ошибки,
выводит подробную информацию об ошибке, используя traceback."""

import traceback

def convert_to_int(input_string):
    # ваш код здесь
    try:
        return int(input_string)
    except Exception as e:
        print("Произошла ошибка")
        traceback.print_exc()


# Тестовый пример
convert_to_int("abc")