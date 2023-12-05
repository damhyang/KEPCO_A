# name = ["may", "kein", "kain", "radi"]
# yearning = [5, 10, 1, 3]
# photo = [["may", "kein", "kain", "radi"],
#          ["may", "kein", "brin", "deny"], 
#          ["kon", "kain", "may", "coni"]]

# def solution(name, yearning, photo):
#     dic={}
#     for i in name :
#         dic[i] = yearning[name.index(i)]
#     return dic
# """answer
# {'may': 5, 'kein': 10, 'kain': 1, 'radi': 3}"""


#     for j in photo :
#         for k in j :
#             score_k = []
#             score_k = .append(dic.get(k))
           
            

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],
         ["may", "kein", "brin", "deny"], 
         ["kon", "kain", "may", "coni"]]

dic={}

score_2=[]
for i in name :
    dic[i] = yearning[name.index(i)]


for j in photo :
    score_1=0
    for k in j :
        
        score = dic.get(k,0)
        score_1 = score_1 + score
    score_2.append(score_1)
print(score_2)
    
      
#result = result + i
#dic에서 바꿔준 후 더함.