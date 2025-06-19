"""Валидация пароля

Напишите функцию для валидации пароля с исользование raise.

Пароль должен соответствовать следующим требованиям: минимум 8 символов, должен содержать хотя бы одну цифру и
одну букву. Если пароль не соответствует требованиям, сгенерируйте исключение с соответствующим сообщением."""

import string

all_digits = string.digits

def validate_password(password):
    # ваш код здесь
    if not isinstance(password, str):
        raise TypeError("Пароль должен быть строкой")

    if len(password) < 8:
        raise ValueError("Пароль должен иметь длину не менее 8 символов")

    has_digits = any(char in all_digits for char in password)
    if not has_digits:
        raise ValueError("Пароль должен содержать хотя бы одну цифру")

    has_letters = any(char.isalpha() for char in password)
    if not has_letters:
        raise ValueError("Пароль должен содержать хотя бы одну букву")

    return "Пароль валиден"


# Тестовый пример
print(validate_password("password123"))  # Ожидаемый вывод: Пароль валиден.
print(validate_password("pass"))  # Ожидаемый вывод: ошибка


# Тестовый пример
print(validate_password("password123"))  # Ожидаемый вывод: Пароль валиден.
print(validate_password("pass"))  # Ожидаемый вывод: ошибка