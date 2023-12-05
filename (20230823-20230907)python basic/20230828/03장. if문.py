#03장. if문 - 프로그램의 구조(if/ while, for)
#비교 연산자            논리 연산자(여기서의 x,y는 단순히 변수가 아니라 참거짓이 나오는 조건임.)
#   <                     x or y  
#   >                     x and y
#   ==                    not x
#   !=
#   <=
#   >=


#in / not in + (리스트, 튜플, **딕셔너리, 문자열)
# 있다 없다라는 불자료형으로 변환시킴.

# if [- else] (else가 필수는 아님)
# if - elif - .... [- else]
#else (x)
#elif (x)


######################################################################################33

money=True
#money는 변수이고, 돈의 유무를 money로 변수명을 적음.
#값이 True이므로 볼 자료형이다.
#돈이 있다는 뜻이다.
#숫자1도 True와 같음.

if money:
#돈이 있으면
    print("택시를 타고 가라")

else:
#돈이 없으면
    print("걸어가라")

##############################################################################
money=False
#돈이 없다는 뜻이다.
#숫자0도 False와 같음.

if money:
#돈이 있으면
    print("택시를 타고 가라")

else:
#돈이 없으면
    print("걸어가라")

###############################################################################

#비교연산자를 사용한 조건문(if 뒤에 조건이 온다.)
money=2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#들여쓰기(스페이스 4칸)를 해야하는 부분을 잘 지켜야한다.
#:(콜론)을 사용한다.
#같은 문장은 같은 들여쓰기를 해야한다.

########################################################################
if money:
    print(money)
    print("taxi")
    print("ok")
    
if money:
    print(money)
    print("taxi")
print("ok")

#이 경우, print문을 조건문 아래가 아니라, 그 자체로 본다면 에러는 생기지 않음.
#다만, 책에서의 IDLE프로그램에서는  앞에 <<<, ...이 있기 때문에 오류가 발생함.
#에러 중, syntax 문법 오류, indent 띄어쓰기 오류
#Tap과 공백은 혼용하면 VSC에서는 문제 없긴 하지만 안되는 프로그램이 있다. 
#:을 하면 저절로 imdent가 된다.
#:이 없으면 오류가 나옴.
#다른 언어는 ;으로 문장의 끝을 알리며, 수행문을 인지시킨다.

#########################################################################################
x=3; y=2
# x=3, y=2는 에러나옴. ; 사용
print(x>y)
print(x<=y)
print(x==y)
print(x!=y)

x=2; y=2
print(x>=y)
print(x<=y)

###########################################################################################

a=8
b=5

if ((a==8) or (b==4)) :
# 조건식이 복잡해 진다면 소괄호를 이용해 조건문을 정리할 수 있다.
# # ex, if ((a==8) or (b==4)):
    print("ok")
else:
    print('nothing')
    ##########################################################################################
    
# 산술연산자는 int->int으 값을 주지만, 문자열-> 참거짓을 준다.
x='1'
y='2'
print(x>y)
print(x<y)


print('a'>'b')
print('a'<'b')

print('aa'>'ab')
print('aa'<'ab')

print("나현웅">="모대현")
print(len("나현웅")>=len("모대현") )
print(len("나현웅")!=len("모대현") )
print(len("나현웅")==len("모대현") )


#문자열(문장)도 아스키코드에 의해 대소 구분가능.
#참인 조건이 있으면, 거짓인 조건도 있어야한다.

##################################################################

pocket = ["card", "cellphone", "money"]

if ("card" not in pocket) :
    print("walk")
else :
    print("bus")

#프로그램이 맞는지를 보려면 반대 상황의 경우도 입력하여 맞게 수행하는지 확인할 것!

pocket = ["cellphone", "money"]

if ("card" not in pocket) :
    print("walk")
else :
    print("bus")

###############################################################################

pocket = ["card", "cellphone", "money"]

if ("card" in pocket) :
    pass
#pass는 구현중으로 일단은 먼저 실행시키는 용도.

else :
    print("walk")
    
#############################################################################
pocket = ["card", "cellphone", "money"]

if ("card" in pocket) :
    print("bus")

#else없어도 됨.
################################################################################

pocket = ["card", "cellphone", money]
money = 4000

# card 택시 or 버스 / money 택시(6000원 이상인 경우) or 버스 / 뚜벅이

# 택시탈 조건 : card(o) or money >=6000
# 버스탈 조건 : 1600<= money <6000
# 다 아니면 걷기
pocket = ["card", "cellphone", money]
money = 4000

if "card" in pocket : 
    print("taxi")

elif money>6000 :
    print("taxi")
elif 1600<=money<6000 :
# (1600<=money) and (money<6000)
    print("bus")
else :
    print("walk")
###################################################################
pocket = ["cellphone", money]
money = 1000

if "card" in pocket : 
    print("taxi")
elif money>6000 :
    print("taxi")
elif 1600<=money<6000 :
    print("bus")
else :
    print("walk")

#####################################################################
#교수님 코드
pocket = ["card", "cellphone", money]
money = 8000

if ("card" not in pocket) and (money<1600):
    print("walk")
elif (money<6000):
    print ("bus")
else :
    print("taxi")
    
###############################################################################
## OOP(객체지향)->재사용성 + 협업 : 코드를 재사용하면서 협업을 함.
## 클래스와 함수를 배워야함.
################################################################################
# (30%)개발 문서(요구분석서->설계도면&계약서)
#      개발계획서(역할분담)
# (30%)변수명 함수명 클래스명 모듈명 통일
# (20%)코딩
# (20%)검증
###############################################################################
#변수명은 영어로.
# 변수명            / 변수명() : 함수명, 클래스명
# pocket            / Pocket()
# customerpocket    /CustomerPocket()     (카멜법)
# customer_pocket                         (스네이크법)
# 소문자             / 대문자

#################################################################################
#약자 
#idx <- index
#cnt <- count
#res <- result

#남이 쉽게 식별할 수 있도록, 한줄에 몰아쓰기나 약자를 최소화한다.그리고 재귀함수 사용X, for문의 삼중중첩을 자제

# 파일명=클래스명
# 클래스명(파일명)은 대문자로, 변수명은 소문자로, 붙여쓰기, 풀네임으로 작성할 것.
####################################################################
# True (1), False (0)으로 치환
# (3>5)  < 10  -> True
##########################################################################
#특정 점수를 입렸했을 때 학점으로 변환
score=int(input("Enter your score: "))
##정수형
#score=input("Enter your score: ")
##문자열
#input()
#input("")
#input은 받아서 변환(반환)이 필요할 경우. 사용.

if score >90:
    grade = "A"
elif score>=80:
    grade = "B"
else:
    grade = "Fail"

print(grade)

##########################################################################
score=int(input("Enter your score: "))
if score >90:
    grade = "A"
if score>=80:
    grade = "B"
if score>=70:
    grade = "C"
if score>=60:
    grade = "D"
if score<60:
    grade = "F"

print(grade)
#####################################
# 순서를 거꾸로 집어넣음.
score=int(input("Enter your score: "))
if score<60:
    grade = "F"
if score>=60:
    grade = "D"
if score>=70:
    grade = "C"
if score>=80:
    grade = "B"
if score >90:
    grade = "A"
    
print(grade)
######################################
# 조건을 "<=??<"으로 범위를 지정하여 해당하는 조건을 하나만 함.
######################################
#if score >90:
#    grade = "A"
#   대신에 print(grade)를 각 조건마다 썼다면 문제점을 더 빨리 찾을 수 있었을 것이다.
score=int(input("Enter your score: "))
if score >90:
    print("grade = A")
if score>=80:
    grade = "B"
if score>=70:
    grade = "C"
if score>=60:
    grade = "D"
if score<60:
    grade = "F"
print(grade)
###############################################

print(3>5)

print("%d" %(3>5))

print(f"{3>5}")

Bool=3 in [2,4,6]
print(f"{Bool}")
