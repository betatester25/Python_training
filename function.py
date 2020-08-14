

def quad():
    x = int(input('Введите любое число: '))
    print('Квадрат этого числа равен', x**2)
    return x**2



def return_string(x):
    y = str(x)
    return y



"""
Функция multiply принимает на вход результат функции division и умножает его на 4
"""

def division(x):
    return int(int(x)/2)

def multiply(x):
    return division(x) * 4


def magic_float():
    while True:
        try:
            inputing = float(input('Введите любое число: '))
        except ValueError:
            print('Вы ввели не число')
        if inputing == 0:
            break



magic_float()





