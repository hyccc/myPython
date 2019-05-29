"""
输入一个正整数判断它是不是素数

Author: Ethan
Date: 2019-05-17
"""
import math

number = int(input('请输入一个数：'))
num = int(math.sqrt(number))

for i in range(2, num+1):
    if number%i == 0:
        is_Prime = False
        break
    else:
        is_Prime = True

if is_Prime and number != 1:
    print('%i 是素数' % number)
else:
    print('%i 不是素数' % number)