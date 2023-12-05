# 매점의 판매이익을 극대화해보자       최대한 팔자 = 거스름돈이 < 700원(포켓몬빵)
# 포켓몬빵: 700원, 아.아: 3100원, 컵라면: 1200원

# 9300 < i * 700 + j * 1200 + k * 3100 <= 10000

result = [ ]
cnt = 0; total = 0
for i in range(1, (10000//700)+1):
    for j in range(1, ((10000-700*i)//1200)+1):
        for k in range(1, ((10000-700*i-1200*j)//3100)+1):
            total = total + 1
            changes = 10000 -(700*i)-(1200*j)-(3100*k) #잔돈을 구하는 변수, 총 합계금액
            if (changes >= 0) and (changes < 700):
                cnt = cnt + 1 #경우의 수 계산하는 변수
                print(f'[{cnt}] 포켓몬빵을 {i}개 구매하고', end=',')
                print(f'컵라면을 {j}개 구매하고', end=',')
                print(f'커피를 {k}개 구매해서 잔돈이 {changes}만큼 남았습니다.')
                result.append([cnt, i, j, k, changes])
print(total)

print(result)
#
print( [ List[4] for List in result] )
print( [ List[0] for List in result] )

print(sorted(result, key=lambda x: x[4]))

sort_result = { }
#  cnt  p   K   c  cha  
# [[1, 1, 5, 1, 200], [2, 2, 2, 2, 0],[3, 3, 1, 2, 500],[4, 3, 4, 1, 0],[5, 4, 3, 1, 500], [6, 6, 2, 1, 300], [7, 8, 1, 1, 100]]
# for List in result:                     # [1, 1, 5, 1, 200]
#     if List[-1] not in sort_result:     # List[-1] = 200 (잔돈, sort_result 딕셔너리의 key)
#         sort_result[List[-1]] = [ ]
#     #            key      = Value
#     sort_result[List[-1]].append(tuple(List))

# print(sort_result)

# Key_list = list(sort_result.keys())
# Key_list.sort()

# for key in Key_list:
#     for List in sort_result[key]:
#         print(f'[{List[0]}] 포켓몬빵을 {List[1]}개 구매하고', end=',')
#         print(f'컵라면을 {List[2]}개 구매하고', end=',')
#         print(f'커피를 {List[3]}개 구매해서 잔돈이 {List[4]}만큼 남았습니다.')