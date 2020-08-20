

d = ['1_D', '2_D', '3_D', '4_D', '5_D', '6_D', '7_D', '8_D', '9_D', '10_D', 'Q_D', 'J_D', 'K_D', 'A_D']

s = ['1_S', '2_S', '3_S', '4_S', '5_S', '6_S', '7_S', '8_S', '9_S', '10_S', 'Q_S', 'J_S', 'K_S', 'A_S']

c = ['1_S', '2_S', '3_S', '4_S', '5_S', '6_S', '7_S', '8_S', '9_S', '10_S', 'Q_S', 'J_S', 'K_S', 'A_S']

h = ['1_H', '2_H', '3_H', '4_H', '5_H', '6_H', '7_H', '8_H', '9_H', '10_H', 'Q_H', 'J_H', 'K_H', 'A_H']



table_cards = ["10_S", "7_S", "9_H", "4_S", "3_S"]
hand_cards = ["K_S", "Q_S"]




total_cards = table_cards + hand_cards
test = []

for i in total_cards:
    x = i.split('_')[1]
    test.append(x)

if test.count('D') >= 5 or test.count('S') >= 5 or test.count('C') >= 5 or test.count('H') >= 5:
    print('flush!')
else:
    print('no flush!')
















"""
count = 0

for i in total:
    if i in d:
        count += 1
    if count >= 5:
        print('У вас flash')

for x in total:
    if x in s:
        count += 1
    if count >= 5:
        print('У вас flash')


for y in total:
    if y in c:
        count += 1
    if count >= 5:
        print('У вас flash')

 
for a in total:
    if a in h:
        count += 1
    if count >= 5:
        print('У вас flash')


"""
