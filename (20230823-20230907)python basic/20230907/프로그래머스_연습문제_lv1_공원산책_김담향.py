park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]

# result = [2,1]

##공원크기 확인하고 그 시작점을 찾기 
#row는 행(가로), column은 열(세로)
#(0,0)부터 시작

maxsize_park=[len(park)-1, len(park[0])-1]  #직사각형이니까 len(park[0])-1이 col의 maxsize가 된다.

for i in range(len(park)) :
    for j in range(len(park[i])) :
        if park[i][j] == 's':
            row = int(i)
            col = int(j)


##위치 이동
for k in routes :
    direction = routes[k][0]
    size = routes[k][2]
    if route[0] == 'N' : row = row - routes[k][2]
    if route[0] == 'S' : row = row + routes[k][2]
    if route[0] == 'W' : col = col - routes[k][2]
    if route[0] == 'E' : col = col + routes[k][2]
    
    if len(park)-1 - row >0 and maxsize_park[1] - locate[1] >0 : 
        go_row = 



##장애물을 만나는지 확인
