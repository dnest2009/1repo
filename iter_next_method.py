class FRange:
    def __init__(self, start=0.0,stop=0.0,step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self
    

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

class FRange2D:  
    def __init__(self, start=0.0,stop=0.0,step=0.0, rows=5):
        self.rows = rows
        self.fr = FRange(start,stop,step)

    def __iter__(self):
        self.value = 0
        return self
    
    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration
        

fr = FRange2D(0, 2, 0.5, 4)
for row in fr:
    for x in row:
        print(x, end=" ")
    print()

def square_numbers():
    try:
        while True:  # Безкінечний цикл для прийому чисел
            number = yield  # Отримання числа через send()
            square = number ** 2  # Піднесення до квадрата
            yield square  # Повернення результату
    except GeneratorExit:
        print("Generator closed")

# Створення і старт генератора
gen = square_numbers()
# Ініціалізація генератора
next(gen)  # Або gen.send(None), щоб стартувати
# Відправлення числа в генератор і отримання результату
result = gen.send(10)  # Повинно повернути 100
print(f"Square of 10: {result}")
# Перехід до наступного очікування
next(gen)
# Відправлення іншого числа
result = gen.send(9)  # Повинно повернути 25
print(f"Square of 5: {result}")

next(gen)
result = gen.send(8) 
print(f"Square of 5: {result}")
next(gen)
result = gen.send(8) 
print(f"Square of 5: {result}")
# Закриття генератора
gen.close()


def filter_lines(keyword):
    print(f"Looking for {keyword}")
    try:
        while True:  # Нескінченний цикл, де генератор чекає на вхідні дані
            line = yield  # Отримання рядка через send()
            if keyword in line:  # Перевірка на наявність ключового слова
                yield f"Line accepted: {line}"
            else:
                yield None
    except GeneratorExit:
        print("Generator closed")

if __name__ == "__main__":
    # Створення і старт генератора
    gen = filter_lines("hello")
    next(gen)  # Потрібно для старту генератора
    messages = ["this is a test", "hello world", "another hello world line", "hello again", "goodbye","hello___098"]
    hello_messages = []
    # Відправлення даних у генератор
    for message in messages:
        result = gen.send(message)  # Відправляємо повідомлення в генератор
        if result:  # Додаємо результат тільки якщо він не None
            hello_messages.append(result)
        next(gen)  # Продовжуємо до наступного yield: інструкція line = yield

    # Закриття генератора
    gen.close()
    print(hello_messages)
