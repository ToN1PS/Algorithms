# Функция для построения таблицы "плохих" символов
def build_bad_char_table(pattern):
    table = {}
    # Проходим по всем символам в шаблоне, кроме последнего
    for i in range(len(pattern) - 1):
        # Вычисляем значение для таблицы "плохих" символов и сохраняем его по ключу символа
        table[pattern[i]] = len(pattern) - 1 - i
    print("таблица плохих символов:", table)
    return table

# Основная функция Бойера-Мура-Хорспула
def boyer_moore_horspool(text, pattern):
    bad_char_table = build_bad_char_table(pattern)
    m = len(pattern)  # Длина шаблона
    n = len(text)     # Длина текста
    i = m - 1         # Индекс в шаблоне
    j = m - 1         # Индекс в тексте
    
    # Цикл по тексту
    while j < n:
        if pattern[i] == text[j]:  # Если символы совпадают
            if i == 0:             # Если достигли начала шаблона
                return j            # Возвращаем индекс начала найденной подстроки
            i -= 1
            j -= 1
        else:
            # Получаем сдвиг из таблицы "плохих" символов для текущего символа текста
            skip = bad_char_table.get(text[j], m)
            j += skip
            i = m - 1
    return -1  # Подстрока не найдена

# Текст и подстрока для поиска
text = "This is a sample text for searching."
pattern = "sample"

# Выполнение поиска и вывод результата
result = boyer_moore_horspool(text, pattern)
if result != -1:
    print(f"Pattern found at index {result}")
else:
    print("Pattern not found")
