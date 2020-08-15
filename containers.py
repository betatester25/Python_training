

my_love_music = ['hip-hop', 'r&b', 'pop']
my_love_songs = ['We gonna be legends', 'Survivor', 'High Upon High']


index = 0
music = {}

for i in range(len(my_love_music)):

    music[my_love_music[index]] = my_love_songs[index]
    index += 1

print(music)


places = [(47.222078, 39.720349), (43.585525, 39.723062)]

my_info = {'рост': 175,
            'вес': 72,
            'любимый актер': 'Jason Statham',
            'профессия': 'programming'}


def about_me():

    my_info = {'рост': 175,
               'вес': 72,
               'любимый актер': 'Jason Statham',
               'профессия': 'programming'}

    question_about_me = input('Введите, что хотите узнать обо мне: ')

    if question_about_me in my_info:
        print(my_info[question_about_me])
    else:
        print('Эта информация недоступна')

