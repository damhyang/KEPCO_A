money = 4000
pocket = [ 'paper', 'cellphone', money, 'card' ]
#card 택시 or 버스 / money 택시 or 버스 / 뚜벅이
#if money >= 6000:
# if money in pocket: #택시 - card(o) or money >= 6000
#     print("택시를 타고 가라")
# elif 'card' in pocket: #버스 - 1600<= money < 6000
#     print("버스를 타고 가라")
# else: 
#     print("걸어간다")


# True (1)  False (0) 으로 치환
# (3>5) < 10    -> 


#특정 점수를 입력했을때 > 학점으로 변환
score = int(input("Enter your score: "))

if score >= 90:
    grade = 'A'
if score >= 80:
    grade = 'B'
if score >= 70:
    grade = 'C'
if score >= 60:
    grade = 'D'
if score < 60:
    grade = 'F'

print(grade)