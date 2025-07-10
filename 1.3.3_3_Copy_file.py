"""Копирование файла

Напишите программу для копирования содержимого из файла original.txt
в новый файл copy.txt с пометкой в тексте, что новый файл это копия."""

# Создание файла original.txt для вашего удобства
with open("original.txt", "w", encoding="utf-8") as file:
    file.write("This is the original file content.")


# Здесь напишите вашу реализацию решения задания
with open("original.txt", "r", encoding="utf-8") as file:
    content = file.read()

with open("copy.txt", "w", encoding="utf-8") as f:
    f.write("This is the copy file of the original file content.")



with open("copy.txt", "a", encoding="utf-8") as ff:
    ff.write(content)



# with open("copy.txt", "r", encoding="utf-8") as fr:
#     res = fr.read()
#     print(res)