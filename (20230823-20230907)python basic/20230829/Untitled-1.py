alphabet = 'abcdefghijklmnopqrstuvwxyz'

name = input("write down your name in english: ")
print("[1]")
for i in alphabet:  #a-z까지 하나씩 탐색
    count=0
    for j in name:
        if i == j:
            count=count+1  #증가식
    print(f"{i} : {name.count(i)}", end = "|")