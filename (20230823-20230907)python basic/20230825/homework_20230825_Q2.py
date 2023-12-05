# Q2='hello python!'을 역순으로 출력하라.
Q2='hello python!'
##(문자열)자료형을 리스트로 바꾼 후, reverse함수로 역순으로 바꾸자.
Q2_list=list(Q2)
print(Q2_list)

 Q2.reverse()
 print(Q2.reverse())
    
Q2_reversed = list(reversed(Q2))
print(Q2_reversed)

answer="".join(Q2_reversed)
print(answer)

# solution2 [::-1]
# SLUTION3 POP과 dppend를 이용하기