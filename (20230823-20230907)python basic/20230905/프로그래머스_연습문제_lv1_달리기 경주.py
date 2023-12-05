
players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
### 정답 = ["mumu", "kai", "mine", "soe", "poe"]
    
    
#리스트형(1)
def solution(players, callings):
    for player in callings:   # player = 'kai'
        # idx 찾기
        idx = players.index(player)   # idx = 3
        # idx-1 <-> idx의 선수 이름을 상호변경하기
        players[idx-1], players[idx] = players[idx], players[idx-1]  # 파이썬만 가능(리스트 내에서만) # players[2], player[3] = player[3], players[2]
    return players                                                   # 리스트 내에서 자리 바꿈 가능.
print(solution(players, callings))
"""answer
['mumu', 'kai', 'mine', 'soe', 'poe']"""

#리스트형(2)
def solution(players, callings):
    for player in callings:     # player = 'kai'
        # idx 찾기
        idx = players.index(player)  # idx = 3  
        # idx-1 <-> idx의 선수 이름을 상호변경하기
        players[idx] = players[idx-1] # players[3] = player[2]
        players[idx-1] = player       # players[2] = 'kai'
    return players
print(solution(players, callings))
"""answer
['mumu', 'kai', 'mine', 'soe', 'poe']"""

#리스트형(3)
def solution(players, callings):
    for player in callings:             # player = 'kai'
        # idx 찾기
        idx = players.index(player)     # idx = 3 
        # idx-1 <-> idx의 선수 이름을 상호변경하기
        players.pop(idx)                 #player[3]을 제거
        players.insert(idx-1, player)    #제거된 것을 인덱스를 -1을 통해 앞당겨 재 작성
    return players
print(solution(players, callings))     
"""answer
['mumu', 'kai', 'mine', 'soe', 'poe']"""
   

        
#dic형_1개(1)
def solution(players, callings):
# 등수와 관련된 dic 생성하기
    rank = {1:"mumu", 2:"soe", 3:"poe", 4:"kai", 5:"mine" }
    for player in callings:
        swich = rank[players.index(player)]
        rank[players.index(player)] =player
        rank[players.index(player)+1] = swich
        players = list(rank.values())
    return players
print(solution(players, callings))       
"""answer
['mumu', 'kai', 'mine', 'soe', 'poe']"""

#dic형_1개(2)
def solution(players, callings):
# 등수와 관련된 dic 생성하기
    rank = {1:"mumu", 2:"soe", 3:"poe", 4:"kai", 5:"mine" }
    for player in callings:
        rank[players.index(player)+1] =rank[players.index(player)]
        rank[players.index(player)] = player
        players = list(rank.values())
    return players   
print(solution(players, callings))  
"""answer
['mumu', 'kai', 'mine', 'soe', 'poe']"""

   
#dic형_2개(1)
def solution(players, callings):
    for player in callings:
        rank = {1:"mumu", 2:"soe", 3:"poe", 4:"kai", 5:"mine" }
        name = {"mumu":1, "soe":2, "poe":3, "kai":4, "mine":5}
        rank[name[player]] = rank[players.index(player)]
        rank[players.index(player)] = player
        players = list(rank.values())
    return players
print(solution(players, callings))  
"""answer
['mumu', 'kai', 'mine', 'soe', 'poe']"""

#dic형_2개(2)
def solution(players, callings):
    rank = {}
    name = {}
    for idx, player in enumerate(players):  #아래의 형태 만드는 for문
        rank[player] = idx+1                #rank = {1:"mumu", 2:"soe", 3:"poe", 4:"kai", 5:"mine" }
        name[idx+1] = player                #name = {"mumu":1, "soe":2, "poe":3, "kai":4, "mine":5}

        idx = name[player] #내 등수에서 -1 하기
        front_player = rank[idx-1] #내 등수 앞선수의 이름
        
###########
    return players
print(solution(players, callings))  
        

나중에 꼭 해보기
#dic에서 자료를 뽑을 때 for문으로 key의 이름순으로 정렬되게 하기#
#저절로 정리되서 나오기도 함.#
