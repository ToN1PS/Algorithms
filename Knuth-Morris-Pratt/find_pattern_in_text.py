class SubstringSearch:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.pattern_length = len(pattern)
        self.text_length = len(text)
        self.prefix_function = [0] * self.pattern_length

    def _compute_prefix_function(self):
        j = 0
        for i in range(1, self.pattern_length):
            while j > 0 and self.pattern[i] != self.pattern[j]:
                j = self.prefix_function[j - 1]
            if self.pattern[i] == self.pattern[j]:
                j += 1
            self.prefix_function[i] = j

    def _search(self) -> int:
        self._compute_prefix_function()
        i = 0
        j = 0

        while i < self.text_length:
            if self.text[i] == self.pattern[j]:
                i += 1
                j += 1
                if j == self.pattern_length:
                    return i - j  # Возвращаем позицию, с которой начинается вхождение
            else:
                if j > 0:
                    j = self.prefix_function[j - 1]
                else:
                    i += 1
        return -1  # Вхождение не найдено

    def find(self) -> str:
        result = self._search()
        if result != -1:
            return(f"Образ найден, начиная с позиции {result}")
        else:
            return("Образ не найден")


# Пример использования класса
text = "лилилось лилилась"
pattern = "лилила"

substring_search = SubstringSearch(text, pattern)
print(substring_search.find())
