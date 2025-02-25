import math

class Derivate:
    def __init__(self, func):
        self.__counter = 0
        self.__fh = func
    
    def __call__(self, x, dx=0.0001, step = 1, *args, **kwargs):
        self.__counter += step
        return f"Похідна: {(self.__fh(x + dx) - self.__fh(x))/dx}  count:{self.__counter}"

@Derivate                 #Декоратор для обчислення похідної
def df_sin(x):
    return math.sin(x)    # можна викликати і так -  df_sin = Derivate(df_sin)


print(df_sin (math.pi/3))
print(df_sin (math.pi/2))
print(df_sin (math.pi/4))

class SmartCalculator:
    def __init__(self, operation='add'):
        self.operation = operation

    def __call__(self, a, b):
        if self.operation == 'add':
            return a + b
        elif self.operation == 'subtract':
            return a - b
        else:
            raise ValueError("Невідома операція")

add = SmartCalculator('add')
print(add(5, 3))  # 8

subtract = SmartCalculator('subtract')
print(subtract(10, 7))  # 3

