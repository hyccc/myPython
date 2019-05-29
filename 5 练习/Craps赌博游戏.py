'''
Craps赌博游戏

规则：玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；
如果点数和为2、3或12，则玩家输庄家胜。
若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜；
若掷出的点数和为7则庄家胜。

author: Ethan
'''
import random


def dice():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    return x + y


if __name__ == '__main__':
    i = 1
    first = dice()
    if first == 7 or first == 11:
        print("掷色子{}次，和为{}，玩家胜".format(i, first))
    elif first == 2 or first == 3 or first == 12:
        print("掷色子{}次，和为{}，庄家胜".format(i, first))
    else:
        print("掷色子第{}次，和为{}，无人获胜".format(i, first))
        while True:
            i += 1
            throw_dice = dice()
            if throw_dice == first:
                print("掷色子第{}次，和为{}，玩家胜".format(i, throw_dice))
                break
            elif throw_dice == 7:
                print("掷色子第{}次，和为{}，庄家胜".format(i, throw_dice))
                break
            else:
                print("掷色子第{}次，和为{}，无人获胜".format(i, throw_dice))

def name():
    print(__name__)