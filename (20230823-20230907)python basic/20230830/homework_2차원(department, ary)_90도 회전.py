ary=[[],[],[],[],[]]
cnt = 0
for i in range(5):     #빈리스트를 가져올 index
    for j in range(5): #반복수
        cnt=cnt+1 
        ary[i].append(cnt)     #ary=[[],[],[],[],[]]
                               #      1  2  3  4  5  임시로 ary안의 요소를 명칭하였을 때,
                               # ary[0]=[1]번째 리스트 요소에 1,2,3,4,5이 들어간다. / ary[1] = [2]6,7,8,9,10
print(ary)
"""answer
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]"""


for i in range(5):     
    for j in range(5): 
        print("%2d" %(ary[5-j-1][i]), end=" ") #ary[0]=[1,2,3,4,5] / ary[1] = [6,7,8,9,10]
    print()
"""answer
 1  2  3  4  5 
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25"""

"""#온라인 검색 결과
def rotate_2d(list_2d):
    n = len(list_2d) # 행 길이 계산
    m = len(list_2d[0]) # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n-i-1] = list_2d[i][j]
    return new"""