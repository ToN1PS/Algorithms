


class BoyerMooreHorspool:
    def __init__(self, pattern):
        self.pattern = pattern
        self.bad_char_table = self._build_bad_char_table()

    def _build_bad_char_table(self):
        table = {}
        # Проходим по всем символам в шаблоне, кроме последнего
        for i in range(len(self.pattern) - 1):
            # Вычисляем значение для таблицы "плохих" символов и сохраняем его по ключу символа
            table[self.pattern[i]] = len(self.pattern) - 1 - i
        return table

    def search(self, text):
        m = len(self.pattern)  # Длина шаблона
        n = len(text)         # Длина текста
        i = m - 1             # Индекс в шаблоне
        j = m - 1             # Индекс в тексте

        # Цикл по тексту
        while j < n:
            if self.pattern[i] == text[j]:  # Если символы совпадают
                if i == 0:                  # Если достигли начала шаблона
                    return j - m + 1       # Возвращаем индекс начала найденной подстроки
                i -= 1
                j -= 1
            else:
                # Получаем сдвиг из таблицы "плохих" символов для текущего символа текста
                skip = self.bad_char_table.get(text[j], m)
                j += skip
                i = m - 1
        return -1  # Подстрока не найдена

# Пример использования
pattern = "example"
text = "This is an example of the Boyer-Moore-Horspool algorithm."
bmh = BoyerMooreHorspool(pattern)
result = bmh.search(text)
if result != -1:
    print(f"Подстрока найдена в позиции {result}.")
else:
    print("Подстрока не найдена.")
