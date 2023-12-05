dic=dict()
for element in 'abcdefghijklmnopqrstuvwxyz':
    #dic[key] = value
    if element not in dic:
        dic[element] = 0
    #print(dic)

name = input("당신의 이름: ")
for element in name:
    dic[element] = dic[element] + 1
    print(dic)

