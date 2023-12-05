# 이름을 입력 받아서 a부터 z까지 알파벳이 볓개 쓰여있는지 출력하는 프로그램 작성

"""내가 직접 작성
request_name = "write down your name in english: "
name_writing = str(input(request_name))
name_lower = name_writing.lower()
character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in character:
    print("spell %s : %d" %(i, name_lower.count(i)))
"""

"""#방법1-1
alphabet = 'abcdefghijklmnopqrstuvwxyz'

name = input("write down your name in english: ")

for i in alphabet:
    count=0
    for j in name:
        if i == j:
            count=count+1 
    print(i, ":", count)
"""

#방법1-2 : alphabet과 name을 일일히 매치하여 일치할 경우 cout를 하는 방법.
"""alphabet = 'abcdefghijklmnopqrstuvwxyz'

name = input("write down your name in english: ")
print("[1]")
for i in alphabet:  #a-z까지 하나씩 탐색
    count=0
    for j in name:
        if i == j:
            count=count+1  #증가식
    print(f"{i} : {name.count(i)}", end = "|")"""

""" #answer#
[1]
a : 0|b : 0|c : 0|d : 1|e : 0|f : 0|g : 3|h : 1|i : 1|j : 0|k : 0|l : 1|m : 0|n : 2|o : 2|p : 0|q : 0|r : 0|s : 0|t : 0|u : 0|v : 0|w : 0|x : 0|y : 0|z : 0|
"""


#방법2: count()함수를 활용
"""alphabet = 'abcdefghijklmnopqrstuvwxyz'

name = input("write down your name in english: ")
print("[2]")
for i in alphabet:
    print(f"{i} : {name.count(i)}", end = "|")"""

""" #answer#
[2]
a : 0|b : 0|c : 0|d : 1|e : 0|f : 0|g : 3|h : 1|i : 1|j : 0|k : 0|l : 1|m : 0|n : 2|o : 2|p : 0|q : 0|r : 0|s : 0|t : 0|u : 0|v : 0|w : 0|x : 0|y : 0|z : 0|
"""

# 위 방법(방법1,2)은 name에 없는 알파벳도 다 확인해야하는 단점이 있음.
# 이에 이름에 있는 알파벳만 확인하게 하는 방법을 생각해볼 수 있다.

# 그 방법으로 name에 있는 알파벳만을 이용하여 카운트하는 방법이 있다.
#name = "honggildong"

#그래서 이름순대로 확인을 하면, 중복되는 알파벳에 대해서도 중복하여 작성하게 된다.
"""h :
o :
n :
g :
g :
i :
l :
d :
o :
n :
g :
"""
#방법3: 중복제거
#이에 #중복을 제거하려면 list(set())함수를 사용한다.
"""
name = input("write down your name in english: ")
name_list=list(set(name))
print("[3]")
for i in name_list:
    print(f"{i} : {name.count(i)}", end = "|")
"""
""" #answer#
[3]
n : 2|o : 2|h : 1|i : 1|g : 3|l : 1|d : 1|
"""
""" 
#만일 알파벳 순으로 정리되기를 원하면  sort를 사용한다.

name = input("write down your name in english: ")
name_list=list(set(name))
name_list.sort()
print("[3]")
for i in name_list:
    print(f"{i} : {name.count(i)}", end = "|")
"""

""" #answer#
[3]
d : 1|g : 3|h : 1|i : 1|l : 1|n : 2|o : 2|
"""


#딕셔너리 자료형
"""리스트나 튜플처럼 순서적으로 요소값을 구하지 않고, Key를 통해 Value를 얻는다.

#구조
dic(딕셔너리 변수이름) = {Key1 : Value1, Key2 : Value2}
Value에 리스트를 넣을 수 있다.

#딕셔너리에 딕셔너리 쌍(Key:Value) 추가와 삭제
#추가
dic = {} 일 떄,
dic[key] = Value 를 해주면
dic = {key:Value}가 되며 이와 같이 딕셔너리 쌍이 추가된다.
#삭제
dic = {key:Value}일 때,
del dic[key]를 하면
dic = {} 가 되며 이와 같이 딕셔너리 쌍이 삭제된다.

#딕셔너리 자료형에서는 인덱싱이 안되고 오직, key로 value를 불러온다.

딕셔너리에 중복되는 key로 value값을 넣으려고 하면, 먼저 넣은 자료는 무시되어 버린다.
즉, key는 중복이 안된다.

#딕셔너리 관련 함수.
##딕셔너리자료.keys() : key리스트를 만들기
##딕셔너리자료.values() : key리스트를 만들기
##딕셔너리자료.items() : 딕셔너리 쌍(Key:Value) 리스트를 만들기
"""


#딕셔너리 자료형을 이용한 이름의 알파벳 갯수 찾기(1)
"""
name = input("write down your name in english: ")
dic={} #dic() / {Key1 : Value1, Key2 : Value2}
print("[dict]")
for key in name :
    if key not in dic:  #key가 dic에 없는 경우.
        dic[key]=1
    else:                #key가 dic에 있는 경우.
        dic[key]=dic[key]+1
        
for key in dic.keys():
        print(f"{key} : {dic[key]}", end = "|")
"""

"""answer
[dict]
h : 1|o : 2|n : 2|g : 3|i : 1|l : 1|d : 1|"""


#딕셔너리 자료형을 이용한 이름의 알파벳 갯수 찾기(2)
"""
name = input("write down your name in english: ")
dic={} #dic() / {Key1 : Value1, Key2 : Value2}
print("[dict]")
for key in name :
    if key not in dic:  #key가 dic에 없는 경우.
        dic[key]=0
        dic[key]=dic[key]+1
    else:                #key가 dic에 있는 경우.
        dic[key]=dic[key]+1
        
for key in dic.keys():
        print(f"{key} : {dic[key]}", end = "|")
"""

"""answer
[dict]
h : 1|o : 2|n : 2|g : 3|i : 1|l : 1|d : 1|
"""

#딕셔너리 자료형을 이용한 이름의 알파벳 갯수 찾기(3)
"""
name = input("write down your name in english: ")
dic={} #dic() / {Key1 : Value1, Key2 : Value2}
print("[dict]")
for key in name :
    if key not in dic:  #key가 dic에 없는 경우.
        dic[key]=[]
        dic[key].append(key)
    else:                #key가 dic에 있는 경우.
        dic[key].append(key)
        
for key in dic.keys():
        print(f"{key} : {dic[key]}", end = "|")
"""

"""answer
[dict]
h : ['h']|o : ['o', 'o']|n : ['n', 'n']|g : ['g', 'g', 'g']|i : ['i']|l : ['l']|d : ['d']|

#해당 결과값을 len()함수를 이용하여 갯수를 세어 알파벳 갯수를 확인 할 수 있다.
"""

# #딕셔너리 자료형을 이용한 이름의 알파벳 갯수 찾기(최종정리)

# name = input("write down your name in english: ")
# dic={} 
# print("[dict]")
# for key in name :
#     if key not in dic:
#         dic[key]=0              # dic[Key] = []                                           
#         dic[key]=dic[key]+1     # dic[Key].append(key)     
#     else:                
#         dic[key]=dic[key]+1     # dic[Key].append(key)    
#     print(dic)
        
# for key in dic.keys():
#         print(f"{key} : {dic[key]}", end = "|")


# """answer
# write down your name in english: honggildong
# [dict]
# {'h': 1}
# {'h': 1, 'o': 1}
# {'h': 1, 'o': 1, 'n': 1}
# {'h': 1, 'o': 1, 'n': 1, 'g': 1}
# {'h': 1, 'o': 1, 'n': 1, 'g': 2}
# {'h': 1, 'o': 1, 'n': 1, 'g': 2, 'i': 1}
# {'h': 1, 'o': 1, 'n': 1, 'g': 2, 'i': 1, 'l': 1}
# {'h': 1, 'o': 1, 'n': 1, 'g': 2, 'i': 1, 'l': 1, 'd': 1}
# {'h': 1, 'o': 2, 'n': 1, 'g': 2, 'i': 1, 'l': 1, 'd': 1}
# {'h': 1, 'o': 2, 'n': 2, 'g': 2, 'i': 1, 'l': 1, 'd': 1}
# {'h': 1, 'o': 2, 'n': 2, 'g': 3, 'i': 1, 'l': 1, 'd': 1}
# h : 1|o : 2|n : 2|g : 3|i : 1|l : 1|d : 1|
# """

#value값을 나중에 추가하기.
dic=dict()
for element in 'abcdefghijklmnopqrstuvwxyz':     # dic[Key] = value
    if element not in dic:
        dic[element] = 0
    print(dic)
"""answer
{'a': 0}
{'a': 0, 'b': 0}
{'a': 0, 'b': 0, 'c': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0}     
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}"""


name = input("your name :")
for element in name:
    dic[element] = dic[element] + 1
    print(dic)
"""answer
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 1, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 1, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 1, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 1, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 1, 'o': 1, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 1, 'h': 1, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 1, 'o': 1, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 2, 'h': 1, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 1, 'o': 1, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 2, 'h': 1, 'i': 1, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 1, 'o': 1, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 2, 'h': 1, 'i': 1, 'j': 0, 'k': 0, 'l': 1, 'm': 0, 'n': 1, 'o': 1, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 0, 'f': 0, 'g': 2, 'h': 1, 'i': 1, 'j': 0, 'k': 0, 'l': 1, 'm': 0, 'n': 1, 'o': 1, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 0, 'f': 0, 'g': 2, 'h': 1, 'i': 1, 'j': 0, 'k': 0, 'l': 1, 'm': 0, 'n': 1, 'o': 2, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 0, 'f': 0, 'g': 2, 'h': 1, 'i': 1, 'j': 0, 'k': 0, 'l': 1, 'm': 0, 'n': 2, 'o': 2, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 0, 'f': 0, 'g': 3, 'h': 1, 'i': 1, 'j': 0, 'k': 0, 'l': 1, 'm': 0, 'n': 2, 'o': 2, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
"""