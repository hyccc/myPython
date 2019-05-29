# project: 
# author: Ethan
# time: 2019/

for i in range(1, 9):
    for j in range(1, i+1):
        print('{} * {} = {}'.format(i, j, i*j), end='\t')
    print()
