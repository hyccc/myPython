'''
打印各种三角形图案
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: Ethan
'''

row = int(input("请输入行数："))

for i in range(row):
    for j in range(1, i+1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j > row - i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

for i in range(row):
    for j in range(row*2-1):
        if j <= row + i - 1 and j >= row - i + 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

