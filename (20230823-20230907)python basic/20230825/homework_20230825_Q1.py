# Q1='1 2 3 4 5 6'의 문자열의 합을 구해라.
Q1='1 2 3 4 5 6'

##solution. 문자열을 리스트로 바꾸자.(1) : Q1_split
###1개로 된 문자열을 split으로 별개의 요소로 나눠 리스트형 자료화함.
Q1_split = Q1.split(" ")
    #print(Q1_split)

##solution. 문자열을 리스트로 바꾸자.(2) : Q1_list
###list()를 이용하여 문자열을 리스트로 바꿈.
Q1_list=list(Q1)
    #print(Q1_list)

###list내의 ' '을 제거하기 위해 .cout(' ')로 센 후, 그 갯수 만큼 .remove(' ')로 제거.
Q1_list.count(' ')
    #print(Q1_list.count(' '))

Q1_list.remove(' ')
Q1_list.remove(' ')
Q1_list.remove(' ')
Q1_list.remove(' ')
Q1_list.remove(' ')
    #print(Q1_list)

##문자열을 정수형으로 바꾸자.(1)
###요소의 갯수를 셈.(결과 6)
len(Q1_split)
    #print(len(Q1_split))

###6개의 요소를 indexing하여 쪼갠 다음 각각에 int()를 하여 
    #fail# answer=Q1_split[0]+Q1_split[1]+Q1_split[2]+Q1_split[3]+Q1_split[4]+Q1_split[5]
answer=int(Q1_split[0])+int(Q1_split[1])+int(Q1_split[2])+int(Q1_split[3])+int(Q1_split[4])+int(Q1_split[5])
print(answer)

answer1=list(map(int, Q1_split))
print(answer1)
