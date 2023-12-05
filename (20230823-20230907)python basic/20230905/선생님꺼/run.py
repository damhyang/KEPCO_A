players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

result = ["mumu", "kai", "mine", "soe", "poe"]


def solution(players, callings):
    answer = []

    for player in callings:
        #idx 찾기
        idx = players.index(player)
        
        players[idx] = players[idx-1]
        players[idx-1] = player
        #players[idx], players[idx-1] = players[idx-1], players[idx]
        # players[3] = players[2] 
        # players[3] = "poe" 
        print(players)
        ['mumu', 'soe', 'poe', 'poe', 'mine']
        # ["mumu", "soe", "poe", "poe", "mine"]
    return answer

solution(players, callings)