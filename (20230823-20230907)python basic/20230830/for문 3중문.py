# 리스트 안에 리스트
# [[],[],[]] #2차원 배열

# for 3중문
"""
포켓몬빵   700원
아아      3100원
컵라면    1200원

받은 돈에 대해 최대한으로 팔 수 있는 조합(잔돈을 최소화 시키는 방법) 
"""

# 나의 생각
"""
money_gest = int(input("insert money: "))

price = {price_bread : 1500, price_coffee : 3100, price_lamen : 1200}
number = {number_bread : 1500, number_coffee : 3100, number_lamen : 1200}
"""
"""
number_bread = i
number_coffee = j
number_lamen = k


sale = {price[price_bread]}*{i} + {price[price_coffee]}*{j} + {price[price_lamen]}*{k}
charge = {money_gest} - {sale}
charge >= 0

i=[]
for i in range(100):
    if ({money_gest} - {price[price_bread]}*{i})>=0 :
"""

# 선생님의 해결방식

#매점의 판매이익을 극대화해보자.
#최대한 팔자 => 거스름돈이 가장 싼 포켓몬빵(700원)보다 적으면 된다.

# 9400 <= i*700 + j*1200 + k*3100 <=10000

# i     j    k
# 0개  8개  0개
# 0개  7개  0개


#먼저 각각의 물건을 최대로 살 수 있는 갯수을 몫을 사용하여 구하고, 0개부터 최대로 살 수 있는 갯수까지 구매한 후의 잔돈을 프린트 하여보자. 
"""
cnt = 0
for i in range((10000//700)+1):
    cnt = cnt +1
    charges = 10000- (700*i)
    print(f'{cnt}포켓몬빵을 {i}개 구매해서 잔돈이 {charges}만큼 남았습니다.')
    

    
for j in range((10000//1200)+1):
    cnt = cnt +1
    charges = 10000- (1200*i)
    print(f'{cnt}라면을 {j}개 구매해서 잔돈이 {charges}만큼 남았습니다.')
    
for k in range((10000//3100)+1):
    cnt = cnt +1
    charges = 10000- (3100*k)
    print(f'{cnt}아아을 {k}개 구매해서 잔돈이 {charges}만큼 남았습니다.')
"""    
    
# 잔돈으로 다음 물건을 사고, 또 그 잔돈으로 다음 물건을 산다.
#i,j,k는 각자에게 영향을 준다.
# 따라서 for문을 종속시킨다.

"""
cnt = 0; total = 0
for i in range(1, (10000//700)+1):   
    for j in range(1, (10000//1200)+1):
        for k in range(1, (10000//3100)+1):
            total = total +1
            cnt = cnt + 1 #경우의 수 계산하는 변수
            changes = 10000 - i*700 - j*1200 - k*3100 #잔돈을 구하는 변수, 총 합계금액
        
            print(f'{cnt}포켓몬빵을 {i}개 구매하고', end="," )
            print(f'라면을 {j}개 구매하고', end=",")
            print(f'아아을 {k}개 구매해서 잔돈이 {changes}만큼 남았습니다.')
            
print(total)"""

##총 연산은 336번, 출력된 값은 336개
##위 대로 연산하면 잔돈이 음수가 나오는데 잔돈이 음수가 나오지 않게 하고자 하면
# ##(그 이유는 i,j,k의 range 설정시에 종속된 남은 잔돈이 아니라 10000으로 하였기 때문이다.)
##이를 if문을 써서 잔돈이 양수인 경우만 남기는 방식으로 고쳐보면 아래와 같다.
"""
cnt = 0; total = 0
for i in range(1,(10000//700)+1):   
    for j in range(1,(10000//1200)+1):
        for k in range(1,(10000//3100)+1):
            total = total +1
            changes = 10000 - i*700 - j*1200 - k*3100 #잔돈을 구하는 변수, 총 합계금액
            if (changes >= 0) and (changes <700):    
                cnt = cnt + 1 #경우의 수 계산하는 변수
        
                print(f'{cnt}포켓몬빵을 {i}개 구매하고', end="," )
                print(f'라면을 {j}개 구매하고', end=",")
                print(f'아아을 {k}개 구매해서 잔돈이 {changes}만큼 남았습니다.')
print(total)"""


##총 연산은 336번, 출력된 값은 7개     
#다만 이 방식은, 출력값을 확 줄어든다.
#이번에는 연산도 줄여보기 위해 i,j,k의 range 설정을 바꿔보자.

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
print(total)

 ##총 연산은 27번, 출력된 값은 7개 