
name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],
         ["may", "kein", "brin", "deny"], 
         ["kon", "kain", "may", "coni"]]

#1번  
def solution(name, yearning, photo):
    return [sum(yearning[name.index(j)] for j in i if j in name) for i in photo]
           #sum(                                               ) for  i   in photo
           #sum(                       List                    ) for list in photo                      
print(solution(name, yearning, photo))
"""answer
[19, 15, 6]"""

#3번


#2번
def solution(name, yearning, photo) :
    answer = []
    dic = {name[x]:yearning[x] for x in range(len(name))}
    for List in photo:
        temp = []
        for panme in List:
            temp.append(dic.get(panme,0)) 
        answer.append(sum(temp))
    return answer

print(solution(name, yearning, photo))
"""answer
[19, 15, 6]"""
