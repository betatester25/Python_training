
while True:
    x = int(input('Введите любое число от 1 до 50: '))

    if x <= 10:
        print('Число {} меньше или равно 10'.format(x))
    elif x > 10 and x <= 25:
        print('Число {} где-то между 10 и 25'.format(x))
    elif x > 25 and x <= 50:
        print('Число {} больше 25'.format(x))
    else:
        print('Вы ввели слишком большое число. Программа завершена.')
        break

