from General_solver import equal

count = 0
arr = equal(3, 7, -7, -4)
print("Q = " + str(round(arr[3], 3)), "R = " + str(round(arr[4], 3)), "S = " + str(round(arr[5], 3)))
for i in arr:
    if count < 3:
        print("x" + str(count) + " = " + str(round(i, 3)))
        count += 1

a = 3
mass = ["Q", "R", "S"]
while True:
    print(mass[a-3] + " = " + str(round(arr[a], 3)))
    a += 1
    if a < 6:
        continue
    break


from human.Human import Human
from human.Woman import Woman

a = Human('Vovkas', 'Pomeloffs')
b = Human('Artem', 'Rozhkoff')
c = Woman('Marina', 'Petrova')
print()
print("===============================")
d = Woman.reproduce(a, c)

b.work()
b.eat()
c.eat()
c.Shopping()
a.fishing()
b.fishing()

print(a.getName(), b.getName(), c.getName(), d.getName())
print()
print("===============================")
