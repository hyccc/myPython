'''
计算指定的年月日是这一年的第几天

思路：
首先要判断 闰年（29天） 还是 平年（28天）
记录下每个月的天数，（我选择字典来存储）然后计算天数！

'''


def judge_year(year):
    if year % 400 == 0 and year % 4 == 0:
        return {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    else:
        return {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def total_day(y, m, d):
    for i in range(1, m):
        day = y.get(i) + d
    return day


if __name__ == '__main__':
        y = int(input("输入年份："))
        year = judge_year(y)

        month = int(input("输入月份："))
        while True:
            if month < 1 or month > 12:
                month = int(input("输入错误，重新输入月份："))
            else:
                break

        date = int(input("输入日期："))
        while True:
            if date < 0 or date > year.get(month):
                date = int(input("输入错误，重新输入日期："))
            else:
                break

        print(total_day(year, month, date))

#
#
# def is_leap_year(year):
#     """
#     判断指定的年份是不是闰年
#
#     :param year: 年份
#     :return: 闰年返回True平年返回False
#     """
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
#
# def which_day(year, month, date):
#     """
#     计算传入的日期是这一年的第几天
#
#     :param year: 年
#     :param month: 月
#     :param date: 日
#     :return: 第几天
#     """
#     days_of_month = [
#         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     ][is_leap_year(year)]
#     total = 0
#     for index in range(month - 1):
#         total += days_of_month[index]
#     return total + date
#
#
# def main():
#     print(which_day(1980, 11, 28))
#     print(which_day(1981, 12, 31))
#     print(which_day(2018, 1, 1))
#     print(which_day(2016, 3, 1))
#
#
# if __name__ == '__main__':
#     main()