"""Проверка типа данных
Напишите функцию, которая принимает два аргумента и умножает их. Используйте блок try-except
для обработки случаев, когда аргументы не являются числами (int/float)."""


def multiply_numbers(a, b):
    try:
        result = a * b
        if not isinstance(result, (int, float)):
            raise TypeError("The result is not a number.")
        return result

    except TypeError as e:
        print(f"Error {e}")

# Тестовый пример
print(multiply_numbers(5, 3))  # Ожидаемый вывод: 15
print(multiply_numbers("world", "hello"))  # Ожидаемый вывод: ошибка
print(multiply_numbers(5, "три"))  # Ожидаемый вывод: ошибка
print(multiply_numbers(10, "20"))  # Ожидаемый вывод: ошибка