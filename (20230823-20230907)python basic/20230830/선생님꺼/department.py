# 자리배치도
Map = [ ['김태영', '김건우', '김담향', '김나영', '이재빈', '', ''],
        ['명하영', '강다솜', '조가영', '이윤주', '조정아', '김동일', ''],
        ['이동훈', '조영승', '윤여록', '김수호', '모대헌', '이승찬', ''],
        ['', '임태환', '박정현', '장성호', '강건희', '유준하', ''] ]

# for elements in Map: 
#     #elements = ['김태영', '김건우', '김담향', '김나영', '이재빈', '', '']
#     print("|".join(elements[::-1]))
#     # print("="*45)

# for elements in Map:
#     for name in elements:
#         if name:
#             print(name, end="|")
#         else:
#             print("%6s"%(name), end='|')
#     print()

# for i in range(25):
#     print(i+1, end=' ')
#     if i % 5 == 4:
#         print()

# cnt=0
# for i in range(5):
#     for j in range(5):
#         cnt = cnt+1
#         # print("%2d"%((5*i)+j+1), end=' ')
#         print("%2d"%(cnt), end=' ')
#     print()

ary = [ [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0] ] # 1~25까지 숫자를 담을

cnt=0
for i in range(5):   
    for j in range(5):
        cnt = cnt + 1
        # ary[i].append(cnt) #ary[0] = [1] 1, 2, 3, 4, 5 / ary[1] = [2] 6,7,8,9,10
        ary[i][j] = ary[i][j] + cnt

print(ary)

for i in range(5):
    for j in range(5):
        print("%2d"%(ary[i][j]), end=' ') #ary[0] = [ 1, 2, 3, 4, 5 ]/ ary[1] = [ 6,7,8,9,10 ]
    print()
