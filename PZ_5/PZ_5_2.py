#Описать функцию TrianglePS(параметры), вычисляющую по стороне a
#равностороннего треугольника его периметр P = 3*a и площадь S = a2 √3/4. С
#помощью этой функции найти периметры и площади трех равносторонних
#треугольников с данными сторонами
def triangle_ps(a):
    p = 3 * a
    s = a * a * 1.732 / 4
    return p, s

try:
    a1 = float(input("a1: "))
    a2 = float(input("a2: "))
    a3 = float(input("a3: "))

    p1, s1 = triangle_ps(a1)
    p2, s2 = triangle_ps(a2)
    p3, s3 = triangle_ps(a3)

    print(p1, s1)
    print(p2, s2)
    print(p3, s3)
except ValueError:
    print("Ошибка")