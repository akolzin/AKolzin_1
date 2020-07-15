import random


class Human:

    def __init__(self, name='Ivan', soname='Ivanov', age=18, money=0):
        self.sex = 'male'
        self.stamina = 150
        self.happiness = 100
        self.name = name
        self.soname = soname
        self.age = age
        self.money = money

    def __del__(self):
        print('экземпляр уничтожен!', self.name)

    def getName(self):
        return self.sex + ' ' + self.name + ' ' + self.soname

    def eat(self):
        if self.money > 0:
            self.money -= 1
            self.stamina += 10
            print(self.name, 'я покушаль! (=', self.money, self.stamina)
        else:
            print(self.name, 'Нету денег! :`(')

    def work(self):
        self.money += 5
        self.stamina -= 10
        self.happiness -= 10

    def fishing(self):
        i = 5 * random.randint(1, 4)
        self.money = self.money + random.randint(-3, -1)
        self.stamina = self.stamina + 5 * random.randint(-4, -1)
        self.happiness = self.happiness + i
        print('Здоровье конечно уже не то', str(self.stamina) + "(150)",'и денег осталось', str(self.money) + "руб",', но здорово было конечно', "(Счастье " + str(self.happiness) + ", прирост " + str(i) + ")")