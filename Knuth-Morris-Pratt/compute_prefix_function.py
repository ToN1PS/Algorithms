class PrefixFunctionCalculator:
    def __init__(self, pattern):
        self.pattern = pattern
        self.prefix_function = [0] * len(pattern)
    
    def calculate_prefix_function(self):
        j = 0
        i = 1
        while i < len(self.pattern):
            if self.pattern[j] == self.pattern[i]:
                self.prefix_function[i] = j + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    self.prefix_function[i] = 0
                    i += 1
                else:
                    j = self.prefix_function[j - 1]
        
        return self.prefix_function
    

# Исходный шаблон
pattern = "лилил"

# Создаем экземпляр класса для вычисления префикс-функции
prefix_calculator = PrefixFunctionCalculator(pattern)

# Вычисляем префикс-функцию и выводим результат
prefix_function = prefix_calculator.calculate_prefix_function()

# Выводим массив префикс-функции
print(prefix_function)

