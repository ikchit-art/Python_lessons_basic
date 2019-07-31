# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
from fractions import Fraction


def action_(str_fr_num):
    minus = 0
    for i in str_fr_num:
        if i == '-':
            minus += 1
    return minus


def is_digits(symbol):
    for i in '1234567890':
        if i == symbol:
            return True


def search_num(str_fr_num):
    i_num = []
    for i in str_fr_num:
        if is_digits(i):
            i_num.append(i)
    return '/'.join(i_num)


def search_fractional(strFractionalNum):
    if strFractionalNum.find(' + ') != -1:
        str_one_num = search_num(strFractionalNum[0:strFractionalNum.find(' + ')])
    elif strFractionalNum.find(' - ') != -1:
        str_one_num = search_num(strFractionalNum[0:strFractionalNum.find(' - ')])
    if strFractionalNum.rfind(' + ') != -1:
        str_two_num = search_num(strFractionalNum[strFractionalNum.rfind(' + '):-1])
    elif strFractionalNum.rfind(' - ') != -1:
        str_two_num = search_num(strFractionalNum[strFractionalNum.rfind(' - '):-1])

    if action_(strFractionalNum) == 0 or action_(strFractionalNum) == 2:
        return Fraction(str_one_num) + Fraction(str_two_num)
    if action_(strFractionalNum) == 1 or action_(strFractionalNum) == 3:
        return Fraction(str_one_num) - Fraction(str_two_num)



print('Программа, выполняет операции (сложение и вычитание) с простыми дробями.\n')
strFractionalNum = input('Введите в стоку простые дробные числа со знаком сложения или вычитания между ними: ')+' '
fr = search_fractional(strFractionalNum)

i_num = []
tr = []
for i in str(fr):
    if is_digits(i):
        i_num.append(i)
    else:
        tr.append(''.join(i_num))
        i_num.clear()
tr.append(''.join(i_num))
i_num.clear()

if int(tr[0]) > int(tr[1]):
    print(f'{int(tr[0]) // int(tr[1])} {int(tr[0]) - int(tr[1])}/{int(tr[1])}')
else:
    print(fr)



# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os


def read_file(file):
    with open(file, "r", encoding='utf-8') as f:
        return f.readlines()


def file_processing(file):
    data = read_file(file)
    a = []
    for i in range(1, len(data)):
        a.append((' '.join(data[i].split())).split())
    return a


def salary(salary_, fact_time, norm_time):
    if int(fact_time) == int(norm_time):
        a = 1
    else:
        a = int(fact_time) - int(norm_time)
    return str(round(int(salary_) + int(salary_) / int(norm_time) * a, 2))


file_workers = os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\workers")
file_hours_of = os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\hours_of")
final = []

for i in file_processing(file_workers):
    for j in file_processing(file_hours_of):
        if i[0] == j[0] and i[1] == j[1]:
            if i[4] == j[2]:
                final.append(''.join(f'{i[0]}, {i[1]}, оклад {i[2]} руб., з/п {salary(i[2], j[2], i[4])} руб., норма {i[4]} час, факт. отработано {j[2]}'))
            else:
                final.append(''.join(f'{i[0]}, {i[1]}, оклад {i[2]} руб., з/п {salary(i[2], j[2], i[4])} руб., норма {i[4]} час, факт. отработано {j[2]}'))

for i in final:
    print(i)

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

file_fruits = os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\fruits.txt")
print(read_file(file_fruits))
check_list = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ"
new_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), r'fruits')
if not os.path.exists(new_path):
    os.makedirs(new_path)

for i in read_file(file_fruits):
    if i != "\n":
        for j in check_list:
            if i[0] == j:
                my_file = open(os.path.join(new_path, fr"fruits_{j}.txt"), "a")
                my_file.write(i)
        my_file.close()
print()

