#03장, for문 (while, for)

#형태
# for i in 반복 가능 객체(iterable,for문과 같은 반복문에 적용가능한 객체) :
#          [리스트(또는 튜플, 문자열)]
#....수행할_문장1
#....수행할 문장2

#여기서 i는 변수임.
#여기서 리스트는 반복 가능한 객체(반복가능객체, iterable)

#교재 p.340 이터레이터와 제너레이터 ->iterable에 대한 설명
# 교재 p.253 range)함수 -> range(시작값, 종료값+1, 증가값)

#자바의 for문과 비교. 

#2-9 :2~8

#range([시작번호, :생략시 0] 마지막번호(-1) [, 증가값 : 생략시 1])
range(1,11)
print(list(range(1,11)))

# #for문으로 1~9까지 출력하기

print(list(range(1,11)))

for i in range(1,10):
    print(i)

# #허용된 약어 순서 : i,j,k,...

# #구구단(for문으로 작성)
"""
구구단(세로로)
구구단(가로로)
구구단(3/3형태)
"""

for i in range(2,10):
    for j in range(1,10):
        print("%d X %d = %d" %(i, j, i*j))

for i in range(2,10):
    for j in range(1,10):
        print("%d X %d = %d" %(i, j, i*j))
    print()
    
for i in range(2,10):
    for j in range(1,10):
        print("%d X %d = %d" %(i, j, i*j))
        print()
        
for i in range(2,10):
    for j in range(1,10):
        print("%d X %d = %d" %(i, j, i*j), end=" ")

for i in range(2,10):
    for j in range(1,10):
        print("%d X %d = %d" %(i, j, i*j), end="")

for j in range(1,10):
    for i in range(2,10):
        print("%d X %d = %d" %(i, j, i*j), end=" ")
    print()

for j in range(1,10):
    for i in range(2,10):
        print("%2d X %2d = %2d" %(i, j, i*j), end=" ")
    print(end="@@@@")

for j in range(1,10):
    for i in range(2,10):
        print("%2d X %2d = %2d" %(i, j, i*j), end=" ")
    print()
    
for i in range(1,10):
    for j in range(2,10):
        print("%d X %d = %d" %(j, i, j*i))
    print()
    
for i in range(1,10):
    for j in range(2,10):
        print("%2d X %2d = %2d" %(j, i, j*i), end=" ")
    print()

##print() : 한줄 띄기
##print(end="  ") : 원하는 내용 적기(띄어쓰기 가능)

#3중 for문(구구단 형태)
    #1단 2단 3단
    #4단 5단 6단
    #7단 8단 9단
    
##데이터의 출력에 대해서의 이해가 필요.

##별 찍기
#
##
###
####
#####
"""
for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()
"""


###
##
#

  #
 ###
#####
 ###
  #

#####
 ###
  #
 ### 
#####

##반복문은 어렵지 않지만 조건문과 을 세우는 것이 어렵다.


"""
리스트 컴프리헨션
교재 내용 따라해보기
[표현식 for 항목 in iterable if conditional(조건식)]
"""
a=[1,2,3,4]
result=[]
##result=[] 은 result=list() 와 같음.
for i in a:
    result.append(i*3)
print(result)


result=[]
for i in range(1,10):
    result.append(i*3)
print(result)

result=[i*3 for i in range(1,10)]
print(result)

result=[i*3 for i in range(1,10) if i%2==0]
print(result)

# while
# 자바코드에서 for문의 구조는 다음과 같이 시작값, 종료값, 증감값으로 구성되어 있다.
# for(int i=1; i<10; i++)   #i++은 1씩 증가한다는 뜻이다.
# while문 역시 위의 자바코드 처럼 시작값, 종료값, 증감값을 모두 적어준다면 무한루프에 빠질 확률이 줄어든다.

i=0
# 시작값
while i<10:
# while의 조건에 종료값이 있음.
    i=i+1
# 증감값
    print("%d X %d = %d" %(2, i, 2*i))

i=1
# 시작값
while True:
    i=i+1
# 증감값
    if i>=10:
        break
# 종료값이 있음.
    print("%d X %d = %d" %(2, i, 2*i))



"""
#while문 - 무한루프의 위험성 때문에 for문을 쓰는 것을 추천
"""

"""
#구조
while+(조건):
...수행문

#while문의 사용처 - 자판기같은 것의 메뉴를 만들어 프로그램이 무한 반복되게 할 경우.
## prompt(menu) = """ """ #""" """은 여러줄 작성시 쓰거나, 주석을 쓸 때도 사용 가능.
## if (조건):
   ....break  #break를 사용하면 반복이 멈춤.

# while True: #옆의 True는 참으로, 결국 (1)로 대신해 쓸 수 있다.
  while(1):
"""

"""정보처리기사->정보관리기술사, 정보보안, 빅데이터분석기사, ADsP(데이터분석 준전문가)"""

"""데이콘 입상, 빅데이터 분산하다 하듑"""
