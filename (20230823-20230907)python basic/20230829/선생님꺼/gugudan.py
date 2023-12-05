# for문으로 1~9까지 출력하기
for i in range(1, 10):
    for j in range(1, 10):
        print("%2dX%2d=%2d" % (i, j, i*j)) #세로 j, i , j*i, end='')
    print() #

# 별찍기
for i in range(5):
    for j in range(i+1):     #->   print( '*' * (i+1))
        print('*', end='')
    print()

