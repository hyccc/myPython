'''
杨辉三角，是二项式系数在三角形中的一种几何排列
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1

思路：
利用坐标来计算杨辉三角！     行（row）列（col）
（0，x）都等于1 ， （x,x）也都等于1，
每一个元素都等于，上一行的两个元素相加：yh[row][col] = yh[row-1][col] + yh[row-1][col-1]
pyton中没有数组，就用双列表来代替。！

反思：
刚开始一直遇到错误，‘IndexError: list index out of range’
list一直为空，数传入不进去。
最后参考答案，发现原答案 传入了一个 None 来保证 list 为空
'''

def main():

    num = int(input("想要计算列数："))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None]*(row+1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row-1][col] + yh[row-1][col-1]
            print(yh[row][col], end=' ')
        print()

if __name__ == '__main__':
    main()




# def main():
#     num = int(input('Number of rows: '))
#     yh = [[]] * num
#     for row in range(len(yh)):
#         yh[row] = [None] * (row + 1)
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
#             print(yh[row][col], end='\t')
#         print()
#
#
# if __name__ == '__main__':
#     main()