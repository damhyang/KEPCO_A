
name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],
         ["may", "kein", "brin", "deny"], 
         ["kon", "kain", "may", "coni"]]

#1번
def solution(name, yearning, photo) :
    dic={}
    for i in name :
        dic[i] = yearning[name.index(i)]
    
    score_2=[]
    for j in photo :
        score_1=0
        for k in j :

            score = dic.get(k,0)
            score_1 = score_1 + score
        score_2.append(score_1)
    return(score_2)

print(solution(name, yearning, photo))
"""answer
[19, 15, 6]"""





