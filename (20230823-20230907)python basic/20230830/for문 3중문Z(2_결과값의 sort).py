##나온 결과값을 잔돈의 오름차순으로 바꿔보자.
##결과값을 이중 리스트의 구조([[]])로 빼보자.
##결과값을 리스트로 정리하는 이유는 리스트가 인덱싱을 

result=[]
cnt = 0; total = 0
for i in range(1,(10000//700)+1):   
    for j in range(1,((10000-i*700)//1200)+1):
        for k in range(1,((10000 - i*700 - j*1200)//3100)+1):
            total = total +1
            changes = 10000 - i*700 - j*1200 - k*3100 #잔돈을 구하는 변수, 총 합계금액
            if (changes >= 0) and (changes <700):    
                cnt = cnt + 1 #경우의 수 계산하는 변수
        
                print(f'{cnt}포켓몬빵을 {i}개 구매하고', end="," )
                print(f'라면을 {j}개 구매하고', end=",")
                print(f'아아을 {k}개 구매해서 잔돈이 {changes}만큼 남았습니다.')
                result.append([cnt, i, j, k, changes])
print(total)

# print(result)
"""answer
[[1, 1, 5, 1, 200], [2, 2, 2, 2, 0], [3, 3, 1, 2, 500], [4, 3, 4, 1, 0], [5, 4, 3, 1, 500], [6, 6, 2, 1, 300], [7, 8, 1, 1, 100]] """

##아래 리스트 컴프리헨션을 사용하여 sorting을 해보려고 했으나 결국 원하는 결과값은 전체를 써야하기 때문이 이 방법을 이용하지 않음.
#리스트 컴프리헨션의 사용
#print([List[4] for List in result])
"""answer
[200, 0, 500, 0, 500, 300, 100]"""
# print([List[0] for List in result])
"""answer
[1, 2, 3, 4, 5, 6, 7]"""

print(f'='*100)
###이미 특정 키를 기준으로 정렬하게 하는 함수가 있습니다.
print(sorted(result, key=lambda x :x[4]))
print(f'='*100)

sort_result={}  # sort_result라는 빈 딕셔너리를 만들고,
for List in result:
    if List[-1] not in sort_result:
        sort_result[List[-1]] = [] # List[-1]은 changes로, 이를 key로 하여 일단 리스트 형태로 value값을 넣기 위해 리스트를 열어준다.
                                   # 그리고 sort_result에는 result상의 자료상에서 changes를 가져온다.
                                   #  key = value 형태임. []이 value에 해당함.
        # print(sort_result)
# """             answer
#                 {200: []}
#                 {200: [], 0: []}
#                 {200: [], 0: [], 500: []}
#                 {200: [], 0: [], 500: [], 300: []}
#                 {200: [], 0: [], 500: [], 300: [], 100: []}"""
    sort_result[List[-1]].append(tuple(List))

#print(sort_result)
"""answer
{200: [(1, 1, 5, 1, 200)], 0: [(2, 2, 2, 2, 0), (4, 3, 4, 1, 0)], 500: [(3, 3, 1, 2, 500), (5, 4, 3, 1, 500)], 300: [(6, 6, 2, 1, 300)], 100: [(7, 8, 1, 1, 100)]} """


key_list = list(sort_result.keys())  # sort_result라는 딕셔너리 안에 있는 키를 리스트형의 자료로 불러온다.
# print(key_list)"""
"""answer
[200, 0, 500, 300, 100]"""

key_list.sort()   #리스트형 자료의 정렬은 sort()함수를 사용한다. 그러면 오름차순으로 정렬된다.
#print(key_list)
"""answer
[0, 100, 200, 300, 500]"""

for key in key_list :    #key_list(잔돈이 정렬된) 라는 리스트의 요소가 반복됨.
    for Tuple in sort_result[key]:    #sort_result[key]는 sort_result라는 딕셔너리에서 key에 맞는 value값이다.
        print(f'{Tuple[0]}포켓몬빵을 {Tuple[1]}개 구매하고', end="," )
        print(f'라면을 {Tuple[2]}개 구매하고', end=",")
        print(f'아아을 {Tuple[3]}개 구매해서 잔돈이 {Tuple[4]}만큼 남았습니다.') 
        




