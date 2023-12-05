#dict 필요성
alphabet = 'abcdefghijklmnopqrstuvwxyz'

name = input("입력하세요: ")
for i in alphabet: #a-z까지 하나씩 탐색
    cnt = 0
    for j in name:
        if i == j:
            cnt = cnt+1 #증가식 
    print(f'{i}:{cnt}', end='|')
print("1]")

for e in alphabet:
    print(f'{e}:{name.count(e)}', end='|')
print('2]')

name_list=list(set(name))
name_list.sort()
for n in name_list:
    print(f'{n}:{name.count(n)}', end='|')
print('3]')

dic={ } #dict() / { key1:value1, key2:value2}
for key in name:
    if key not in dic: #키가 없는가?
        dic[key] = [ ]
        dic[key] = dic[key] + 1
    else: #키가 존재한다. 
        dic[key] = dic[key] + 1

for key in dic.keys():
    print(f'{key}:{dic[key]}', end='|')
print('dict]')