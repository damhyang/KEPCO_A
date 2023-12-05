#Q3='3 a 7 21 z x u b d 0 b b b 2 1 1 1'을 chr과 int로 각각 분류(정렬)
Q3='3 a 7 21 z x u b d 0 b b b 2 1 1 1'

#list함수로 문자열 요소를 리스트로 변경하려 하였으나 띄어쓰기까지 리스트화되어 실패로 간주.
    #fail# list_Q3=list(Q3)
    #fail#print(list_Q3)

split_Q3=Q3.split(" ")
print(split_Q3)

#sort함수를 이용하여 분류(정렬)
#answer1=split_Q3.sort()
#print(answer1)

#sorted로 사용
answer2=sorted(split_Q3)
print(answer2)

final = " ".join(answer2)
print(final)