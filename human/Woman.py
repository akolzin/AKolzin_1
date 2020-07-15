import random

from .Human import Human


class Woman(Human):

    def __init__(self, name='Ivan', soname='Ivanov', age=18, money=0):
        super().__init__(name, soname, age, money)
        self.sex = 'female'
        self.stamina = 100

    @staticmethod
    def reproduce(fother=None, mother=None):
        if fother and mother:
            if type(fother) == Human and type(mother) == Woman:
                print('можно размножаться')
                return Human()
            else:
                print('Алярма! Ахтунги атакуют!!!')
                return None
        print('не хватает одного из родителей!')
        return None

    def eat(self):
        if self.money > 0:
            self.money -= 1
            self.stamina += 5
            print(self.name, 'я покушала! (=', self.money, self.stamina)
        else:
            print(self.name, 'Совсем нету денег на ноготочки! :`(')

    def Shopping(self):
        i = 5 * random.randint(-10, 10)
        self.money = self.money + random.randint(-2, 2)
        self.happiness = self.happiness + i
        print('По шопилась, денег осталась', self.money, 'Счастливая на', self.happiness, "(прирост " + str(i) + ")")