"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version: 0.1
Author: 骆昊
"""
import random

answer = random.randint(1, 100)
print(answer)
while True:
    t = int(input('请猜测0~100中的数字：'))
    if answer > t:
        print('正确答案比较大')
    elif answer < t:
        print('正确答案比较小')
    else:
        print('恭喜你猜对了')
        break
