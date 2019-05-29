"""
设计一个函数，产生指定长度的验证码，由 大小写字母和数字构成

思路：
上一题用的是 字符串，这一次我也用 字符串 来存储 验证码可能出现的所有字符。
然后利用 随机 选择其中的字符来进行组合出需要 验证码

与原答案差别：
我将字符长度写死了！！
原答案用 len（）方法，自动算出最后一个元素的下表 “last_pos = len(all_chars) - 1”
自己还算半天，能不写死的就别写死
"""

import random


def create_code(len):
    code = ''
    content = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                # for i in content:
                #     print(i, end='')
                #     x += 1
                # print(x)           # 此代码数出 一共有 62 个字符  注意：字符标号为 0~61
    for i in range(len):
        x = random.randint(0, 61)    # 注意：只要 下标 所在的字符为空，就会出错。所以要判断好范围
        code = code + content[x]
    return code


code_len = int(input("输入验证码的长度 为："))
print(create_code(code_len))


# import random
#
#
# def generate_code(code_len=4):
#     """
#     生成指定长度的验证码
#
#     :param code_len: 验证码的长度(默认4个字符)
#
#     :return: 由大小写英文字母和数字构成的随机验证码
#     """
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
#     return code