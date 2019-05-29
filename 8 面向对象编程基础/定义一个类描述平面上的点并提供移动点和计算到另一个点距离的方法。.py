'''
定义一个类 描述平面上的点并提供移动点和计算到另一个点距离的方法。

思路：
定义一个 Point 类，提供两个点，一个点是 起始点，一个点是 终点。
需要从 起始点 移动到 终点
'''
from math import sqrt


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x, y):           # 移动到
        self.x = x
        self.y = y

    def move_by(self, dx, dy):         # 移动增量
        self.x += dx
        self.y += dy

    def distance(self, other):       # 点距离
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)

    print(p1.distance(p1))


if __name__ == '__main__':
    main()