#레프리 함수
com=[9, 3, 4]

def refree(com):
    scnt=0
    bcnt=0
    user = []
    while (len(user) != 3):                     #user 숫자 입력받기
        temp = input("숫자 3개를 입력하세요: ")
        if len(list(set(temp.split()))) != 3:
            continue

        for unum in temp.split():
            user.append(int(unum))
    # print(user)
    for i, cnum in enumerate(com):              # scnt, bcnt 판정하기
        for j, unum in enumerate(user):

            #strike
            if (i == j) and (cnum == unum):
                scnt += 1
            elif (cnum == unum):
                bcnt += 1
    
    return scnt, bcnt


test= refree(com)
print(com, test)