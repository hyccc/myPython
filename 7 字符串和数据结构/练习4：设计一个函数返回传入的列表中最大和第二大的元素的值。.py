'''
设计一个函数返回传入的列表中最大和第二大的元素的值

思路：
这是经典的算法问题，如何进行排序，排出最大的元素将其提取出来。（直接用冒泡排序提取出最大的就行）
python中有个 reverse 自动排序的方法，然后提取 （ reverse 是倒序！！记错了）
sort 方法才是排序
'''


list = [51, 3, 85, 38, 62, 78, 50]


def max():
    list.sort()
    list.reverse()
    return list[0], list[1]


print(max())



# def max2(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     for index in range(2, len(x)):
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1, m2