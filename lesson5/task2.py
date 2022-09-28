# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint



def kto_pervi():
    r = randint(1,2)
    print(f'первым ходит игрок {r}')
    return r

def pobeda(i,c):
    if i == 0 and not c%2: print(f'победа вторго игрока')
    elif i == 0 and c%2==1: print(f'победа первого игрока')

def igra(i,c):
    while i != 0:
        if not c % 2:
            print(f'ход второго игрока, осталось {i} конфет')
            h = int(input('введите число от 1 до 28 '))
            if i >= h <= 28: i -= h
            else : print('введите валидное число')


        else:
            print(f'ход первого игрока, осталось {i} конфет')
            h = int(input('введите число от 1 до 28 '))
            if i >= h <= 28: i -= h
            else : print('введите валидное число')


        pobeda(i, c)
        c += 1

    return i

def igra_s_botom(i,c):
    while i != 0:
        if not c % 2:
            print(f'ход второго игрока, осталось {i} конфет')
            h = randint(1,29)
            if i >= h <= 28: i -= h
            else : print('введите валидное число')

        else:
            print(f'ход первого игрока, осталось {i} конфет')
            h = int(input('введите число от 1 до 28 '))
            if i >= h <= 28: i -= h
            else : print('введите валидное число')

        pobeda(i, c)
        c += 1

    return i

def igra_s_umnim_botom(i,c):
    while i != 0:
        if not c % 2:
            print(f'ход второго игрока, осталось {i} конфет')
            h = i%29
            if i >= h <= 28: i -= h
            else : print('введите валидное число')

        else:
            print(f'ход первого игрока, осталось {i} конфет')
            h = int(input('введите число от 1 до 28 '))
            if i >= h <= 28: i -= h
            else : print('введите валидное число')

        pobeda(i, c)
        c += 1

    return i


konfetki = 100

n = int(input(' для игры с человеком введите 1\n для игры с ботом введите 2\n для игры с умным ботом введите 3\n'))
chey_hod = kto_pervi()
if n == 1: igra(konfetki, chey_hod)
elif n == 2: igra_s_botom(konfetki,chey_hod)
elif n == 3: igra_s_umnim_botom(konfetki,chey_hod)
else: print('введите валидное число')