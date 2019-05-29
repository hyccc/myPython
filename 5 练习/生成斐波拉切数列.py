'''
斐波那契数列（Fibonacci sequence），
又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）
以兔子繁殖为例子而引入，故又称为“兔子数列”，
指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
在数学上，斐波纳契数列以如下被以递推的方法定义：
F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）

'''


def fic(n):
    if n >= 3:
        return fic(n-1) + fic(n-2)
    elif n < 3:
        return 1


if __name__ == '__main__':
    while True:
        num = int(input("请输入一个大于等于 3 的整数数："))
        if num < 3:
            print("你输入的数字小于 3，请重新输入")
        elif type(num) != int:
            print("你输入的不是数字，请重新输入")
        else:
            break

    print(fic(num))



