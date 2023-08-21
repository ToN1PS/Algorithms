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
