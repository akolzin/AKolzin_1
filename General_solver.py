import math

# найти корень линейного уравнения
# a*x + b = 0
def lineEqual(a, b):
    if not a == 0:
        return [-b / a]
    return []

# квадратное уравнение
# a*x^2 + b*x + c = 0
def squareEqual(a, b, c):
    # если вдруг уравнение оказалось линейным
    if a == 0:
        return lineEqual(b, c)
    D = b ** 2 - 4 * a * c
    if D == 0:
        return [-b / (2 * a)]
    elif D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return [x1, x2]
    return []

# кубическое уравнение
# a*x^3 + b*x^2 + c*x + d = 0

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    elif x == 0:
        return 0

def cubeEqual(A, b, c, d):

    a = b / A
    b = c / A
    c = d / A
    Q = ((a ** 2) - (3 * b)) / 9
    R = ((2 * a ** 3) - (9 * a * b) + (27 * c)) / 54
    S = (Q ** 3) - (R ** 2)
    if S == 0:
        x1 = (-2 * (R ** 1 / 3)) - (a / 3)
        x2 = (R ** 1 / 3) - (a / 3)
        return [x1, x2, Q, R, S]
    elif S < 0:
        if Q < 0:
            fi = (math.asinh(abs(R) / math.sqrt(abs(Q) ** 3))) / 3
            print(fi)
            x1 = (- 2 * sign(R) * math.sqrt(abs(Q)) * math.sinh(fi)) - (a / 3)
            return [x1, Q, R, S]
        elif Q > 0:
            fi = (math.acosh(abs(R) / math.sqrt(Q ** 3))) / 3
            x1 = (- 2 * sign(R) * math.sqrt(Q) * math.cosh(fi)) - (a / 3)
            return [x1, Q, R, S]
    elif S > 0:
        fi = (math.acos(R / (math.sqrt(Q ** 3)))) / 3
        x1 = (-2 * math.sqrt(Q) * math.cos(fi)) - (a / 3)
        x2 = (-2 * math.sqrt(Q) * math.cos(fi + (math.pi * 2 / 3))) - (a / 3)
        x3 = (-2 * math.sqrt(Q) * math.cos(fi - (math.pi * 2 / 3))) - (a / 3)
        return [x1, x2, x3, Q, R, S]

# общий решатель для уравнений
def equal(a, b, c=None, d=None):
    if not c == None and not d == None:
        return cubeEqual(a, b, c, d)
    if not c == None:
        return squareEqual(a, b, c)
    return lineEqual(a, b)
