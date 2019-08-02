# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os
import shutil


def go_folder():
    folder = input('Введите путь к папке:')
    try:
        os.chdir(os.path.join(directory(), folder))

    except FileExistsError:
        print('Путь не достижим')

    finally:
        print('Успешно перешел ', os.getcwd())


def look_folder():
    print(os.listdir(directory()))


def directory():
    return os.path.dirname(os.path.abspath(__file__))


def create_folder(name):
    if not os.path.exists(os.path.join(directory(), name)):
        os.mkdir(os.path.join(directory(), name))
    print(os.listdir(directory()))


def remove_folder(name):
    try:
        os.path.exists(os.path.join(directory(), name))
    except FileExistsError:
        print('Данная папка уже существует')
        look_folder()
    finally:
        os.rmdir(os.path.join(directory(), name))


while True:
    print('1. Перейти в папку \
        2. Просмотреть содержимое текущей папки \
        3. Удалить папку\
        4. Создать папку')
    command = input('Введите номер команды: ')
    if command == '1':
        go_folder()
    if command == '2':
        look_folder()
    if command == '3':
        remove_folder(input('Введите папку для удаления:'))
    if command == '4':
        create_folder(input('Введите имя папки:'))
    if command != '1' or command != '2' or command != '3' or command != '4':
        continue