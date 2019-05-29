"""
输入两个正整数计算最大公约数和最小公倍数

最大公约数：都可以被两方整除
最小公倍数：两个数的乘积，除以最大公约数

Author: Ethan
Date: 2019-5-17
"""

num1 = int(input('请输入第一个数字：'))
num2 = int(input('请输入第二个数字：'))

if num1 < num2:
    num1, num2 = num2, num1

for factor in range(num1, 0, -1):
    if num1 % factor == 0 and num2 % factor == 0:
        print('{}和{}的最大公约数为{}'.format(num1, num2, factor))
        print('{}和{}的最小公倍数为{}'.format(num1, num2, num1*num2/factor))
        break
