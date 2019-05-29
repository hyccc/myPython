"""
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。
寻找所有水仙花数

author:Ethan
date: 2019-5-18
"""

for factor in range(100, 1000):
    hundred = factor // 100
    ten = factor//10 % 10
    bit = factor % 100 % 10
    if factor == hundred**3 + ten**3 + bit**3:
        print('水仙花数为{}'.format(factor))

