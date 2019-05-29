'''
跑马灯：
让文字像广告屏一样，轮转

思路：
首先想到的是用 列表 来存储内容，然后用列表中的方法，将 第一个元素 调到 最后一个元素
所以 pop 和 append 方法 对列表进行 删除和增加

缺点：
就是操作上麻烦，需要用一个变量 x 来存储 第一个元素（被删除），再添加进 列表， 无疑是多了一些步骤。

原答案思路：
原来答案直接用 字符串 的 切块，直接进行调换位置，简单 明了。

'''
import time




def main():
    list = ['深', '圳', '欢', '迎',  '你', '!', '!', '!']
    while True:
        time.sleep(0.5)

        for i in range(0, 8):
            print(list[i], end=' ')
        print()
        x = list.pop(0)
        list.append(x)


main()



# os.system('clear')
# def main():
#     content = '深圳欢迎你！！！'
#     while True:
#         time.sleep(0.5)
#         print(content)
#         content = content[1:] + content[0]
#
# main()
