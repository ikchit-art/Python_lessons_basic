# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os, shutil


def directory():
    return os.path.dirname(os.path.abspath(__file__))


def create_folder(name, x2):
    for i in range(1, int(x2)+1):
        name_folder = name + str(i).strip()
        if not os.path.exists(os.path.join(directory(), name_folder)):
            os.mkdir(os.path.join(directory(), name_folder))
    print(os.listdir(directory()))


def remove_folder(name,  x2):
    for i in range(1, int(x2)+1):
        name_folder = name + str(i).strip()
        if os.path.exists(os.path.join(directory(), name_folder)):
            os.rmdir(os.path.join(directory(), name_folder))
    print(os.listdir(directory()))


print("Создание папок")
create_folder(input('Введите имя папки: '), input('Введите индекс папок: '))
print("Удаление папок")
remove_folder(input('Введите имя папки: '), input('Введите индекс папок: '))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print('Задача-2:')
print(os.listdir(directory()))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print('Задача-3:')
if os.path.exists(os.path.join(directory(), __file__)):
    shutil.copyfile(os.path.join(directory(), __file__), os.path.join(directory(), f'{__file__}_копия'))
print(os.listdir(directory()))
