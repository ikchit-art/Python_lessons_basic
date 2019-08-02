# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
import random


class Triangle:
    def __init__(self, dot_1, dot_2, dot_3):
        self.dot_1 = dot_1
        self.dot_2 = dot_2
        self.dot_3 = dot_3

    def height(self):
        p = self.perimeter() / 2
        a = triangle_side_lenght(self.dot_1, self.dot_2)
        b = triangle_side_lenght(self.dot_1, self.dot_3)
        c = triangle_side_lenght(self.dot_3, self.dot_2)
        h = (2 / a )* math.sqrt(p * (p - a) * (p - b) * (p - c))
        return round(h, 2)

    def perimeter(self):
        # как можно автоматизировать(упростить) эту операцию? можно ли перебирать переменные в цикле?
        p = triangle_side_lenght(self.dot_1, self.dot_2) + triangle_side_lenght(self.dot_1, self.dot_3) \
              + triangle_side_lenght(self.dot_3, self.dot_2)
        return round(p, 2)

    def square(self):
        s = triangle_side_lenght(self.dot_1, self.dot_2) * self.perimeter() / 2
        return round(s, 2)


def triangle_side_lenght(x, y):
    return round(math.fabs(math.sqrt(((x[0] - x[1]) ** 2) + ((y[0]) - y[1]) ** 2)), 2)


# Вероятно это неправильное решение с точки зрения геометрии
def trapeze_factor(x, y,):
    return round(math.tan((x[0] - y[1]) / (x[0]) - y[1]), 1)


A = (random.randint(0, 9), random.randint(0, 9))
print(A)
B = (random.randint(0, 9), random.randint(0, 9))
print(B)
C = (random.randint(0, 9), random.randint(0, 9))
print(C)
triangle = Triangle(A, B, C)

print(f"Периметр треугольника равен: {triangle.perimeter()} см")
print(f"Высота треугольника равна: {triangle.height()} см")
print(f"Площадь треугольника равна: {triangle.square()} см")


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class Trapeze:
    def __init__(self, dot_1, dot_2, dot_3, dot_4):
        self.dot_1 = dot_1
        self.dot_2 = dot_2
        self.dot_3 = dot_3
        self.dot_4 = dot_4

    def true_trapeze(self):
        if trapeze_factor(self.dot_1, self.dot_2) == trapeze_factor(self.dot_3, self.dot_4) \
                or trapeze_factor(self.dot_2, self.dot_3) == trapeze_factor(self.dot_4, self.dot_1):
            print("Фигура является равнобочной трапецией")
            print(f"Длина отрезка a = {triangle_side_lenght(self.dot_1, self.dot_2)}")
            print(f"Длина отрезка b = {triangle_side_lenght(self.dot_2, self.dot_3)}")
            print(f"Длина отрезка c = {triangle_side_lenght(self.dot_3, self.dot_4)}")
            print(f"Длина отрезка d = {triangle_side_lenght(self.dot_4, self.dot_1)}")
            d = triangle_side_lenght(self.dot_4, self.dot_3)
            a = triangle_side_lenght(self.dot_2, self.dot_1)
            c = triangle_side_lenght(self.dot_4, self.dot_1)
            h = math.sqrt((c ** 2) - ((a - d) ** 2))
            print(f"Площадь = {round(self.perimeter() * h, 2)}")
            print(f"Периметр = {self.perimeter()}")
        else:
            print("Фигура не является равнобочной трапецией")

    def perimeter(self):
        p = triangle_side_lenght(self.dot_1, self.dot_2) + triangle_side_lenght(self.dot_3, self.dot_3) \
              + triangle_side_lenght(self.dot_3, self.dot_4) + triangle_side_lenght(self.dot_4, self.dot_1)
        return round(p, 2)

    def square(self):
        c = triangle_side_lenght(self.dot_4, self.dot_3)
        a = triangle_side_lenght(self.dot_2, self.dot_1)
        s = (c + a) / 2
        return round(s, 2)


A = (random.randint(0, 9), random.randint(0, 9))
B = (random.randint(0, 9), random.randint(0, 9))
C = (random.randint(0, 9), random.randint(0, 9))
D = (random.randint(0, 9), random.randint(0, 9))

print(A)
print(B)
print(C)
print(D)

trapeze = Trapeze(A, B, C, D)
trapeze.true_trapeze()
