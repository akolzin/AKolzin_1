import math
# дз
# a(x**2)+bx-c=0
# 10(x**2)+6x-4=0

a = 10
b = 6
c = -4

D = b**2 - 4 * a * c
print("Дискрименант равен " + str(D))

if D > 0:

    x = (-b + pow(D,0.5))/(2 * a)
    x1 = (-b - math.sqrt(D))/(2 * a)

    print("Первый корень " + str(x) + " и " + str(x * -1), ", второй корень " + str(x1) + " и " + str(x1 * -1))
else:
    print("Отрицательный дискрименант, корней нет!")


