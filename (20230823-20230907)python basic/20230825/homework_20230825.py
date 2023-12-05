# Q1='1 2 3 4 5 6'의 문자열의 합을 구해라.
Q1='1 2 3 4 5 6'

#solution1
##1개로 된 문자열을 나눠 별개의 요소로 나눔.
Q1_split = Q1.split(" ")
    #print(Q1_split)

##요소의 갯수를 셈.
    #print(len(Q1_split))

##6개의 요소를 index를 이용하여 더함.
    #fail# answer=int(Q1_split[0])+int(Q1_split[1])+int(Q1_split[2])+int(Q1_split[3])+int(Q1_split[4])+int(Q1_split[5])
answer=int(Q1_split[0])+int(Q1_split[1])+int(Q1_split[2])+int(Q1_split[3])+int(Q1_split[4])+int(Q1_split[5])
print(answer)

# Q2='hello python!'을 역순으로 출력하라.
Q2='hello python!'
##(문자열)자료형을 리스트로 바꾼 후, reverse함수로 역순으로 바꾸자.
Q2_list=list(Q2)
print(Q2_list)

    #fail# Q2.reverse()
    #fail# print(Q2.reverse())
    
Q2_reversed = list(reversed(Q2))
print(Q2_reversed)

"".join(Q2_reversed)