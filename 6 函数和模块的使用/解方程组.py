# '''
# 解答：x1 + x2 + x3 + x4 = 8  有多少组正整数的解
#
# 转换思路：
# 等同于将 8 个苹果分成四组，每组至少一个苹果有多少种方案
#
# 8个椅子，三个隔板插空问题，C7选三
# '''
#
#
# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fmn = 1
# for num in range(1, m - n + 1):
#     fmn *= num
# print(fm // fn // fmn)

from random import randint


def roll_dice(n=2):
    """
    摇色子

    :param n: 色子的个数
    :return: n颗色子点数之和
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))