'''
我国古代数学家张丘建在《算经》一书中提出的数学问题：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，
问鸡翁、鸡母、鸡雏各几何？
'''

money = 100  # 百钱
total = 100  # 百鸡

for x in range(100):
    for y in range(100):
        for z in range(100):
            if x+y+z == 100 and 5*x + 3*y + 1/3*z == 100:
                print("公鸡有{}只，母鸡有{}只，小鸡有{}只".format(x, y, z))
