from typing import List

# Исходный шаблон
pattern = "лилила"

# Инициализация массива префикс-функции для шаблона pattern
prefix_function = [0] * len(pattern)

# Индекс j для сравнения символов в шаблоне
j = 0

# Индекс i для прохода по шаблону и вычисления префикс-функции
i = 1

# Вычисление префикс-функции для шаблона pattern
while i < len(pattern):
    if pattern[j] == pattern[i]:
        prefix_function[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            prefix_function[i] = 0
            i += 1
        else:
            j = prefix_function[j - 1]

# Вывод массива префикс-функции
print(prefix_function)

# Строка, в которой ищется подстрока
text = "лилилось лилилась"

# Длины шаблона и строки, в которой ищется подстрока
pattern_length = len(pattern)
text_length = len(text)

# Индексы i и j для сравнения символов в строке и шаблоне соответственно
i = 0
j = 0

# Поиск вхождения шаблона pattern в строке text с использованием префикс-функции
while i < text_length:
    if text[i] == pattern[j]:
        i += 1
        j += 1
        if j == pattern_length:
            print("Образ найден")
            break
    else:
        if j > 0:
            j = prefix_function[j - 1]
        else: 
            i += 1

# Если i достигло конца строки, искомый образ не найден
if i == text_length:
    print("Образ не найден")
