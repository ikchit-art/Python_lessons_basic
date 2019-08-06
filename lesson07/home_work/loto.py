#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class TableNum:
    def __init__(self):
        self.list_num = TableNum.gen_table

    def del_num(self, num):
        pass

    @staticmethod
    def draw_table():
        print('------- Ваша карточка --------')
        for i in range(3):
            for j in range(9):
                print("{:>3}".format(TableNum.list_num[0][j]), end='')
            print()
        print('-----------------------------')
        print('---- Карточка компьютера ----')

        for i in range(3):
            for j in range(9):
                print("{:>3}".format(TableNum.list_num[1][j]), end='')
            print()
        print('-----------------------------')

    @property
    def gen_table(self):
        list_num = [random.sample(range(1, 90), 27),
                    random.sample(range(1, 90), 27)]
        for index in range(2):
            for i in random.sample(range(0, 9), 4):
                list_num[index][i] = ''

        return list_num


class Box:
    # def __init__(self):
    #     self.list_del_num = "список зачеркнутых номеров"
    #     self.list_left_keg = "список оставшихся боченков в мешке"

    def gen_keg(self, round_game):
        keg = random.sample(range(1, 90), 89)
        print(f"Выпал боченок: {keg[round_game]} (в мешке {91 - round_game} осталось номеров)")
        return keg[round_game]


class Game(Box):
    def __init__(self, round_game):
        # self.gamer =
        self.r_game = round_game

    def round_game(self):
        k = self.r_game + 1
        return k

    def find_keg(self, list_game):
        x = self.gen_keg(self.round_game())
        return list_game.count(x)


print('Это игра Лото:')
table = TableNum
game = Game(1)
status = False
while not status:
    game.gen_keg(game.round_game())
    table.draw_table()
    check = input('Зачеркнуть цифру? (y/n)')
    if check == 'y':
        status = True
