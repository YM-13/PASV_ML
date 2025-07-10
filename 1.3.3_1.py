"""
Напишите программу, которая запрашивает у пользователя его имя, фамилию и возраст и записывает в файл user.txt."""

data = input("Введите ваши имя, фамилию и возраст, разделяя данные запятой ").split(', ')
with open('user.txt', 'w', encoding='utf-8') as f:
    f.write(f'Имя: {data[0]},\nФамилия: {data[1]},\nВозраст: {data[2]}\n')

with open('user.txt', 'r', encoding='utf-8') as f:
    print(f.read())