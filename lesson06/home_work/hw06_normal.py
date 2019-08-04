# coding=utf-8
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
import random


# class School:
#     def __init__(self):
#         self.classes = self.set_classes()
#
#     def set_classes(self):
#         str_ = 'АБВГД'
#         a = [str(j) + str_[i] for j in range(5, 12) for i in range(0, random.randint(2, len(str_)))]
#         return a
# Ошибка: у класса School нет атрибута classes

class Human:
    def __init__(self, birth_date, name, surname, patronymic):
        self.birth_date = birth_date
        self.name = name
        self.surname = surname
        self.patronymic = patronymic


class Teacher(Human):
    def __init__(self, name, surname, patronymic, birth_date, lesson, classes):
        Human.__init__(self, name, surname, patronymic, birth_date)
        self.classes = classes
        self.lesson = lesson

    def teacher_info(self):
        print('_____________________________________________________________')
        print('Учитель')
        print(f'ФИО: {self.name} {self.patronymic} {self.surname}')
        print(f'Дата рождения: {self.birth_date}')
        print(f'Предмет: {self.lesson}')
        print(f'Ведет классы: {self.classes}')
        print('_____________________________________________________________')


class Students(Human):
    def __init__(self, name, surname, patronymic, birth_date, class_name, mother_name, father_name):
        Human.__init__(self, name, surname, patronymic, birth_date)
        self.class_name = class_name
        self.list_lessons = lessons
        self.mother_name = mother_name
        self.father_name = father_name

    def student_info(self):
        print('_____________________________________________________________')
        print('Ученик')
        print(f'ФИО: {self.name} {self.patronymic} {self.surname}')
        print(f'Дата рождения: {self.birth_date}')
        print(f'Родители: {self.mother_name}, {self.father_name}')
        print(f'Класс: {self.class_name}')
        print('_____________________________________________________________')


str_ = 'АБВГД'
classes = [str(j) + str_[i] for j in range(5, 12) for i in range(0, random.randint(2, len(str_)))]

lessons = ["Математика", "Русский язык", "Литература", "Физкультура", "Иностранный язык", "История", "География",
           "Химия", "Биология", "Информатика", "Логика", "Философия", "Иностранный язык2"]
names = ['Иван', 'Петр', 'Сергей', 'Лев', 'Денис', 'Марк', 'Антон', 'Евгений']
surnames = ['Петров', 'Иванов', 'Сидоров', 'Кузнецов', 'Лопоухов', 'Питонов', 'Дубинин', 'Пучков', 'Распутин',
            'Романов', 'Ленин', 'Насыров', 'Чемборисов']
patronymics = ['Иванович', 'Петрович', 'Сергеевич', 'Львович', 'Денисович', 'Маркович', 'Антонович', 'Евгеньевич']
dates_of_birth = ['12.08.1998', '22.09.1996', '11.12.2002', '12.05.1999', '02.08.2003', '01.01.1993', '12.12.1997',
                  '16.09.2007', '12.11.1996', '07.08.2006', '21.08.1998', '30.04.1996', '28.08.2008', '25.06.1999']
dates_of_birth_adults = ['12.08.1965', '22.09.1978', '11.12.1991', '12.05.1956', '02.08.1969', '01.01.1985']
initials = ['И.А.', 'В.Г.', 'А.А.', 'Д.С.', 'В.Ю.', 'Н.А', 'С.С.', 'Л.М.', 'Ю.Л.']

students = []
teachers = []

for i in range(20):
    male_student = Students(random.choice(names), random.choice(surnames), random.choice(patronymics),
                            random.choice(dates_of_birth), random.choice(classes),
                            (random.choice(surnames) + 'а') + ' ' + random.choice(initials),
                            random.choice(surnames) + ' ' + random.choice(initials))
    students.append(male_student)

for i in range(3):
    group_list = []
    for j in range(random.randrange(4, 5)):
        group_list.append(random.choice(classes))
        while group_list.count(group_list[j]) > 1:
            group_list[j] = random.choice(classes)

    male_teacher = Teacher(random.choice(dates_of_birth_adults), random.choice(surnames), random.choice(patronymics),
                           random.choice(names), random.choice(lessons), group_list)

    for k in range(len(lessons)):
        try:
            if lessons[k] == male_teacher.lesson:
                lessons.pop(k)
        except IndexError:
            pass

    group_list = []
    for j in range(random.randrange(4, 5)):
        group_list.append(random.choice(lessons))
        while group_list.count(group_list[j]) > 1:
            group_list[j] = random.choice(lessons)
    teachers.append(male_teacher)

status = 0

while status != 1:

    print('1 - Информация о всех учениках')
    print('2 - Информация о всех учителях')
    print('3 - Полный список всех классов школы')
    print('4 - Список всех учеников в указанном классе')
    print('5 - Список всех предметов указанного ученика')
    print('6 - ФИО родителей ученика')
    print('7 - Список учителей, преподающий в указанном классе')
    mode = int(input('Что вы хотите сделать?'))

    if mode == 1:
        # Информация о всех учениках
        for student in students:
            student.student_info()

    elif mode == 2:
        # Информация о всех учителях
        for teacher in teachers:
            teacher.teacher_info()

    elif mode == 3:
        # Полный список всех классов школы
        all_groups = []
        for student in students:
            if all_groups.count(student.class_name) == 0:
                all_groups.append(student.class_name)

        print(f'Полный список классов школы. в которых есть хотя бы 1 ученик: {all_groups}')

    elif mode == 4:
        # Список всех учеников в указанном классе
        inp_group = input('Введите класс (в формате "11А"): ')
        students_in_group = []
        for student in students:
            if student.class_name == inp_group:
                students_in_group.append(student.surname + ' ' + student.name[0] + '.' + student.patronymic[0] + '.')
        print(students_in_group)

    elif mode == 5:
        # Список всех предметов указанного ученика
        std_group = ''
        inp_name = input('Введите ФИО ученика (в формате "Сидоров Иван Иванович"): ')
        for student in students:
            if (student.surname + ' ' + student.name + ' ' + student.patronymic) == inp_name:
                std_group = student.class_name

        subjs = []
        for teacher in teachers:
            if std_group in teacher.lesson():
                subjs.append(teacher.subject)

        print(f'Предметы, которые изучает {inp_name}: {subjs}')

    elif mode == 6:
        # ФИО родителей ученика
        std_prnts = []
        inp_name = input('Введите ФИО ученика (в формате "Сидоров Иван Иванович"): ')
        for student in students:
            if (student.surname + ' ' + student.name + ' ' + student.patronymic) == inp_name:
                std_prnts = [student.mother_name, student.father_name]

        print(f'Родители ученика {inp_name}: {std_prnts}')

    elif mode == 7:
        # Список учителей, преподающих в указанном классе
        tchrs = []
        inp_group = input('Введите класс (в формате "11 А"): ')
        for teacher in teachers:
            if inp_group in teacher.classes():
                tchrs.append(
                    str(teacher.surname + ' ' + teacher.name + ' ' + teacher.patronymic + ' (' + teacher.lesson + ')'))

        print(f'Преподаватели, ведущие в классе {inp_group}: {tchrs}')

    end = input('Завершить работу? (y/n)')
    if end == 'y':
        status = 1
