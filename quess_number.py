import random
count = 0

while count < 6:
    user_number = int(input('Попробуйте угадать число от 1 до 50: '))

    if user_number == random.randint(1, 50):
        print('Вы угадали число')
    elif user_number != random.randint(1, 50):
        print('Вы не угадали число')
    count += 1

