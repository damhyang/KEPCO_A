data = [['장려상', 60,1,0,0], 
        ['동상', 70,1,1,5], 
        ['은상', 80,1,1,10], 
        ['금상', 90,1,1,20]]   ##[rank, min_score, trophy, bonus]


#1번 case : 원하는대로 은상만 나오지 않고, 조건에 해당하는 모든게 나옴.
def prize(List, score):
    if score >= List[1]:
        return List[0]

score = 81  ##임의로 넣음
for List in data :
    result = prize(List, score)  
    print(result)  
"""answer
장려상
동상
은상
None"""

#2번 case : 1번 케이스에서 [::-1]을 이용해서 뒤집고, result값이 처음 생기면 break를 걸어서 더이상 값이 없도록 바꾸었다.
def prize(List, score):
    if score >= List[1]:
        return List[0]

score = 81  ##임의로 넣음
for List in (data[::-1]) :  #List는 [rank, min_score, trophy, bonus]와 같다.
## for [rank, min_score, trophy, bonus] in data:  
    result = prize(List, score)
    if result:
        break
print(result)    
"""answer
은상"""

#3번 case : enumerate를 통해 index를 얻어 이를 활용

def prize(idx, List, score):
    if score >= List[1]:
        return 3-idx
    
score = int(input("점수를 입력하세요: "))

for idx, List in enumerate(data[::-1]):
    if prize(idx, List, score):
        break
print(data[3-idx])
"""answer
점수를 입력하세요: 81
['은상', 80, 1, 1, 10]"""


#4번 case 
def prize(List, score):
    if score >= List[1]:
        return True
    
score = int(input("점수를 입력하세요: "))

for idx, List in enumerate(data[::-1]):
    if prize(List, score):
        print(data[::-1][idx])
        break
"""answer
점수를 입력하세요: 81
['은상', 80, 1, 1, 10]"""


#5번 case : 함수()를 사용하지 않고,  
score = int(input("점수를 입력하세요: "))

for [rank, min_score, trophy, bonus,qty] in data:
    if score >= min_score:
        print(f'" 님, ======{rank}=====', end='')
        if qty:
            print(f'상품: 문화상품권 {qty}매')
"""answer
점수를 입력하세요: 81
" 님, ======장려상=====" sla, ======동상=====상품: 문화상품권 5매
" 님, ======은상=====상품: 문화상품권 10매"""            
            
#6번 case : 함수()를 사용하지 않고,  
score = int(input("점수를 입력하세요: "))

for [rank, min_score, trophy, bonus,qty] in data[::-1]:
    if score >= min_score:
        print(f'" 님, ======{rank}=====', end='')
        if qty:
            print(f'상품: 문화상품권 {qty}매')
        break
"""answer
점수를 입력하세요: 81
" sla, ======은상=====상품: 문화상품권 10매"""
    
    
#7번 case : 함수()를 사용하지 않고,  
score = int(input("점수를 입력하세요: "))

for [rank, min_score, trophy, bonus,qty] in data[::-1]:
    if score >= min_score:
        print(f'" 님, ======{rank}=====', end='')
        if qty:
            print(f'상품: 문화상품권 {qty}매')
        print()

        for txt in [rank, qty]:
            if txt:
                print({txt},end="")
            print()
            break
"""answer
점수를 입력하세요: 81
" 님, ======은상=====상품: 문화상품권 10매

{'은상'}
" 님, ======동상=====상품: 문화상품권 5매

{'동상'}
" 님, ======장려상=====
{'장려상'}"""
        

#8번 case : 함수()를 사용하지 않고,  
score = int(input("점수를 입력하세요: "))

for [rank, min_score, trophy, _,qty] in data[::-1]:
    if score >= min_score:
        print(f'" 님, ======{rank}=====', end='')
        if qty:
            print(f'상품: 문화상품권 {qty}매')
        print()
"""answer
점수를 입력하세요: 81
" 님, ======은상=====상품: 문화상품권 10매

" 님, ======동상=====상품: 문화상품권 5매

" 님, ======장려상====="""    
    
    
#9번 case 
def prize(min_score, score):
    if score >= min_score:
        return True
    
score = int(input("점수를 입력하세요: "))
for idx, List in enumerate(data[::-1]):
    if prize(List[1], score):
        print(data[::-1][idx])
        break
"""answer
점수를 입력하세요: 81
['은상', 80, 1, 1, 10]"""