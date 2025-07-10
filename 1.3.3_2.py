"""Анализ данных из файла

Создайте программу, которая читает файл numbers.txt, содержащий числа, каждое на новой строке,
и выводит их сумму, среднее и медиану."""

# Создание файла numbers.txt для вашего удобства
import random
with open("numbers.txt", "w") as file:
    for _ in range(random.randint(10, 20)):
        file.write(f"{random.randint(-10000, 10000)}\n")


# Здесь напишите вашу реализацию решения задания
with open("numbers.txt", "r") as file:

    numberts = list(map(int, file.read().split('\n')[:-1]))
    numberts.sort()
    total = sum(numberts)
    l = len(numberts)
    avarage = total / l
    median = numberts[int(l / 2)]

    print(total, avarage, median, sep='\n')
