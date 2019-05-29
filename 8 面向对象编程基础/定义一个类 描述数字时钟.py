'''
定义一个类，描述数字时钟

思路：
首先，先执行一下原答案，查看结果知道我们需要的结果是什么
看到答案知识普通的在屏幕上，每经过一秒，时间就加上 一秒，并且时间是自己设定的
主要在于练习 类 概念

这样就用1 个类 Clock, 2 个类方法 run, show 来实现
'''
from time import sleep


class Clock():

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def run(self):             # 时钟走动
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0
        if self.hours == 24:
            self.hours = 0

    def show(self):             # 时钟显示
            print("{}:{}:{}".format(self.hours, self.minutes, self.seconds))

def main():
    clock = Clock(23, 59, 52)
    while True:
        sleep(1)
        clock.run()
        clock.show()


if __name__ == '__main__':
    main()