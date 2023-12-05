## 숫자야구 ##

class Numberbaseball:
# 시작화면
    def Start(self) :
        print("="*50)    
        print(" "*20 + "야구 숫자")
        print("="*50)     
    
# 컴퓨터의 답 생성하기
    def Threenumber_com(self) :
        import random
        numlist = [1,2,3,4,5,6,7,8,9]
        self.threenumber_com = random.sample(numlist, 3)
        return self.threenumber_com
    
# user에게 답을 입력하도록 하기
    def Threenumber_user(self) :
        self.threenumber_input_user = input("1~9까지의 숫자를 중복없이 연달아 넣어주세요: ")
        self.threenumber_user = [int(self.threenumber_input_user[0]), 
                                  int(self.threenumber_input_user[1]), int(self.threenumber_input_user[2])]
        return self.threenumber_user

# 숫자 중복없애기
    def Overlap(self, list):
        result = []
        for i in list:
            if i not in result:
                result.append(i)
        return result

# 판정하기
    def Judgement(self, threenumber_com, threenumber_user):
        self.count_strike = 0
        self.count_ball = 0
        for i in range(3):
            for j in range(3):
                if threenumber_user[i] == threenumber_com[j]:
                    if i == j :
                        self.count_strike = self.count_strike + 1
                    if i != j : 
                        self.count_ball = self.count_ball + 1
        print(f"{self.count_strike} Strike  {self.count_ball} Ball")

# user 승리멘트
    def user_win(self):
        print("="*30)    
        print(" "*10 + "시도 {try}회로 10회안에 3strike 찾기 성공 : USER 승리")
        print("="*30) 
        
# user 실패멘트(횟수초과)
    def user_lose(self):
        print("="*30)    
        print(" "*10 + "10회 안에 3strike 찾기 실패 : COM 승리")
        print("="*30) 

#######################################################################################################################

# main 함수
run = Numberbaseball()
start = run.Start()
# # 시작화면
#     def Start(self) :
#         print("="*50)    
#         print(" "*20 + "야구 숫자")
#         print("="*50) 
threenumber_com = run.Threenumber_com()
# 컴퓨터의 답 생성하기
# def Threenumber_com(self) :
#     import random
#     numlist = [1,2,3,4,5,6,7,8,9]
#     self.threenumber_com = random.sample(numlist, 3)
#     return self.threenumber_com
while True : 
    threenumber_user = run.Threenumber_user()
    # user에게 답을 입력하도록 하기
    # def Threenumber_user(self) :
    #     self.threenumber_input_user = input("1~9까지의 숫자를 중복없이 연달아 넣어주세요: ")
    #     self.threenumber_user = [int(self.threenumber_input_user[0]), 
    #                               int(self.threenumber_input_user[1]), int(self.threenumber_input_user[2])]
    #     return self.threenumber_user
    threenumber_user_Overlap=run.Overlap(threenumber_user)
    # # 숫자 중복없애기
    # def Overlap(self, list):
    #     result = []
    #     for i in list:
    #         if i not in result:
    #             result.append(i)
    #     return result
    if len(threenumber_user_Overlap)==3:
        break
 

for k in range(10) :
    judgement = run. Judgement(threenumber_com, threenumber_user_Overlap)
    if (threenumber_com == threenumber_user_Overlap) :
        break