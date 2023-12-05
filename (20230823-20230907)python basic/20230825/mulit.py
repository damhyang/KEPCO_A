# 문자열 자료형을 변수에 저장? 선언?
words = "hobhy"

#words = "hobby"
# "hob"+"b"+"y"                    
# words[:2]+"b"+words[4:]
# words[:2]+"b"+words[-1]
# words[0]+words[1]+words[2]+'b'+words[4]

# 어떻게?    list() 
words_list = list(words)
print(words_list)

words_list[3]='b'
print(words_list)

# 어떻게 문자열로?
print("".join(words_list))




# 피곤한 당신을 위해 준비한 문제!

# Q1='1 2 3 4 5 6'  > 합을 구해라!
# Q2='Hello Python!' 을 !nohtyP olleH  역순으로 출력해라
# Q3='3 a 7 21 z x u b d 0 b b b 2 1 1 1 ' 을 char, int 각각으로 분류(정렬하시오!)

#문자열을 리스트로 변환
    # 0 1 2  3 4 5 6 7 8 9 10 11 12
Q3='3 a 7 21 z x u b d 0 b b b 2 1 1 1 '
#변환된 리스트를 반복문으로 하나씩 가져온다
result=[]
Q3_list=Q3.split()
print(int(Q3_list[0]) + int(Q3_list[2]) +int(Q3_list[3]) +int(Q3_list[13])+int(Q3_list[14])+int(Q3_list[15])+int(Q3_list[16]))
#int(Q3_list[1]) #오류
# int(Q3_list[2])
# int(Q3_list[3])

for element in Q3.split():
#가져온 요소를 int로 형변환시킨다
#오류가 발생하지 않으면 반환한다
    try:
        result.append(int(element))
    except:
        pass

print(result)
sum=0
for i in range(len(result)):
    sum= sum + result[i]

for i in result:
    sum= sum + i




