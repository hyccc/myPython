'''
分析代码：
基类：Fighter   属性：name，hp（hp可以修改）     方法：alive， attack
继承类：Ultraman   属性：mp（可以修改）       方法：attack， huge_attack， magic_attack, resume
        Monster    属性：                     方法：attack


is_any_alive,   判断怪兽是不是活的
select_alive_on,    选一只活着的怪兽
 display_info      显示 ultraman 和 monster 的信息

'''
import random
from abc import ABCMeta, abstractmethod


class Fighter(object, metaclass= ABCMeta):

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp > 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass


class Ultraman(Fighter):

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= random.randint(15, 25)

    def huge_attack(self, other):
        """究极必杀技(打掉对方至少50点或四分之三的血)

        :param other: 被攻击的对象

        :return: 使用成功返回True否则返回False
        """
        if self._mp > 50:
            self._mp -= 50
            injury = other.hp * 3//4
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """魔法攻击

        :param others: 被攻击的群体

        :return: 使用魔法成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= random.randint(15, 25)
            return True
        else:
            return False

    def resume(self):
        incr_point = random.randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp


class Monster(Fighter):

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    def attack(self, other):
        other.hp -= random.randint(10, 20)

    def __str__(self):
        return '~~~%s怪兽~~~' % self.name +\
                '生命值：%d\n' % self.hp


def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive:
            return True
    return False


def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = random.randrange(monsters_len)
        monster = monsters[index]
        if monster.alive:
            return monster


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('UU', 500, 500)

    m1 = Monster('M1', 250)
    m2 = Monster('M2', 500)
    m3 = Monster('M3', 750)
    ms = [m1, m2, m3]

    fight_round = 1

    while u.alive and is_any_alive(ms):
        print('========第%02d回合=======' % fight_round)
        m = select_alive_one(ms)
        skill = random.randint(1, 10)
        if skill <= 6:    # 使用普通攻击
            print('{}使用了普通攻击打了{}'.format(u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点' % (u.name, u.resume()))
        elif skill < 9:   # 使用魔法攻击
            if u.magic_attack(ms):
                print('%s使用了魔法攻击' % u.name)
            else:
                print('%s 使用魔法攻击失败' % u.name)
        else:
            if u.huge_attack(m):
                print('%s使用了大招虐了%s' % (u.name, m.name))
            else:
                print('%s 使用普通攻击打了%s' % (u.name, m.name))
                print('%s 的魔法值恢复了%d点' % (u.name, u.resume()))

        if m.alive > 0:
            print('%s 回击了 %s' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)
        fight_round += 1


    print('\n=========战斗结束=========\n')
    if u.alive:
        print('%s 奥特曼胜利' % u.name)
    else:
        print('怪兽胜利')

if __name__ == '__main__':
    main()