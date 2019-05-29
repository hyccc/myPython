'''
设计一个函数返回给定文件名的后缀名

思路：
首先，给定文件名，并未指出要指定路径。
文件名的特点  "xxx.txt"     找出 点 的后面，即是后缀名

原答案：
1. rfind 方法：
    Python rfind(str, beg=0 end=len(string)) 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1
    str -- 查找的字符串
    beg -- 开始查找的位置，默认为 0
    end -- 结束查找位置，默认为字符串的长度。

2. 有些文件可能没有 点 的存在！
   而且是 最后一个点 的后面才是后缀名！！（没有考虑到）
   所以需要从后往前去搜索，所以 rfind 的方法最适配


反思：
要多看一些方法，记住方法就可以直接使用，节省很多代码量
思考的东西不够深入，经验不够多
'''


def filename_suffix(filename):
    # num = 0
    # for i in filename:
    #     if i == '.':
    #         num += 1
    #         break
    #     num += 1

    # 修改
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        return filename[pos+1:]
    else:
        return ' '


print(filename_suffix('shenme.txt'))




# def get_suffix(filename, has_dot=False):
#     """
#     获取文件名的后缀名
#
#     :param filename: 文件名
#     :param has_dot: 返回的后缀名是否需要带点
#     :return: 文件的后缀名
#     """
#     pos = filename.rfind('.')
#     if 0 < pos < len(filename) - 1:
#         index = pos if has_dot else pos + 1
#         return filename[index:]
#     else:
#         return ''