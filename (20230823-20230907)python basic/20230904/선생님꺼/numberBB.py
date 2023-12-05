import random

class BaseBall():
    def __init__(self):
        self.com = []
        self.cnt = 0
        self.scnt = 0
        self.bcnt = 0

    def start(self): #시작
        print("숫자 야구를 시작합니다.")
        self.com = random.sample(range(1,10), 3)
        self.cnt = 0

    def refree(self):
        user = []

        while (len(user) != 3):                     #중복되지 않은 숫자3개
            temp = input("숫자 3개를 입력하세요: ")
            if len(list(set(temp.split()))) != 3:
                continue
            
            for unum in temp.split():               # user리스트에 int형으로 저장하기
                user.append(int(unum))

        self.cnt += 1
        for i in range(len(user)):              # scnt, bcnt 판정하기
            if self.com[i] == user[i]:
                self.scnt += 1
            elif user[i] in self.com:
                self.bcnt += 1
    
    def end(self): #종료결과 출력
        if self.scnt == 3:
            print("축하합니다. 이기셨습니다.")
            return
        # print(f"[{cnt}] {self.scnt}S {self.bcnt}B")
        print(f"[{self.cnt}] {self.scnt}S {self.bcnt}B      {self.com}")

        self.scnt = 0
        self.bcnt = 0

# main함수 구성
run = BaseBall() #run객체 생성

run.start()

while True:
    run.refree()
    run.end()
    if (run.cnt == 10) or (run.scnt == 3):
        break
