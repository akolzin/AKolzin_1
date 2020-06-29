import math
# дз
# a(x**2)+bx-c=0

a = 10
b = 6
c = -4
print("Уравнение: " + str(a) + "x^2+" + str(b) + "x" + str(c) + "=0")

D = b**2 - 4 * a * c # находим дискреминант
print("Дискрименант равен " + str(D))

if D > 0:
    # находим корни уравнения
    x = (-b + pow(D,0.5))/(2 * a)
    x1 = (-b - math.sqrt(D))/(2 * a)

    print("Первый корень " + str(x) + " и " + str(x * -1), ", второй корень " + str(x1) + " и " + str(x1 * -1))
else:
    print("Отрицательный дискрименант, корней нет!")


