"""Пользовательские исключения

Определите и используйте собственный класс исключения для обработки специфической ошибки в вашем коде, например,
когда пользовательский ввод не соответствует ожидаемому формату."""

"""class ValidationError(Exception): - создание собственного (пользовательского) исключения, которое наследуется 
от встроенного класса Exception.

На практике это значит:
ValidationError становится новым типом ошибки.
Она ведёт себя как обычное исключение (её можно raise, except и т.д.).
Наследование от Exception означает, что это "нормальная" ошибка, которую можно перехватывать в блоках try-except.

class ValidationError(Exception):
    pass

def validate_age(age):
    if age < 0:
        raise ValidationError("Возраст не может быть отрицательным")

try:
    validate_age(-5)
except ValidationError as e:
    print(f"Ошибка валидации: {e}")
    
--> Ошибка валидации: Возраст не может быть отрицательным

Зачем это нужно?
-Чётко разделять типы ошибок (например, ValidationError, PermissionError, ParsingError)
-Делать код более читаемым и предсказуемым
-Упрощать обработку конкретных ошибок:

try:
    ...
except ValidationError:
    handle_validation_issue()
except PermissionError:
    handle_auth_issue()
"""


class ValidationError(Exception):
    # ваш код здесь
    def __init__(self, invalid_value, fild_name="username", message="Неверный тип введенных данных"):
        self.invalid_value = invalid_value
        self.fild_name = fild_name
        self.message = message
        super().__init__(f'{message}: {fild_name} =  {self.invalid_value}')

def validate_username(username):
    # ваш код здесь
    if not isinstance(username, str):
        raise ValidationError(username)

    return "Ввдеденные данные соответствуют требованиям к username"

# Тестовый пример
try:
    print(validate_username("john"))
except ValidationError as e:
    print(f"Ошибка валидации: {str(e)}")
