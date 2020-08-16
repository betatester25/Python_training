"""

for i in 'Чехов':
    print(i)



write = input('Что вы вчера написали? ')
goes = input('Куда вы вчера ходили? ')

print(f'Вчера я написал {write}. Вчера я ходил в {goes}.')



string_with_error = 'олдос Хаксли родился в 1984 году'
word_list = string_with_error.split(' ')
right_word = word_list[0].capitalize()
right_string = right_word + string_with_error.replace('олдос', '')

print(right_string)


x = 'Где это? Кто это? Когда это?'.split(' ')

questions = [x[0]+' '+x[1], x[2]+' '+x[3], x[4]+' '+x[5]]

print(questions)



fox = ['Рыжая', 'лиса', 'перепрыгнула', 'через', 'низкий', 'забор', '.']

one_fox = ' '.join(fox).replace('.', '').strip() + '.'

print(one_fox)



child = 'Ребенок - зеркало поступков родителей'
print(child.replace('о', '0'))

"""
a = 'Хемингуэй'

print(a.index('м'))