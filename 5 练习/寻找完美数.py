'''
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。它所有的真因子（即除了自身以外的约数）的
和（即因子函数），恰好等于它本身。
如果一个数恰好等于它的因子之和，则称该数为“完全数”。第一个完全数是6，第二个完全数是28，第三个完全数是496，
后面的完全数还有8128、33550336等等

author: Ethan
'''

for i in range(1, 1000000000):
    divisor = 0   # 约数
    for j in range(1, i):
        if i % j == 0:
            divisor += j
    if divisor == i:
        print("完美数为{}".format(i))
