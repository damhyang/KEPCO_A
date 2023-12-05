# #1번.
# m = int(input("m: "))
# a = int(input("a: "))

# if a>m :
#     m=a
# a = int(input("a: "))
# if a>m :
#     m=a
# print("가장큰수:", m)

# #2번 : 함수로 바꾸기

# def Maxvalue(*args):
#     maxvalue = 0
#     for i in args:
#         if i > maxvalue:
#             maxvalue=i
#     print(maxvalue)

# Maxvalue(1,2,3,4,5,6)


##그떄그때 value를 받아서 대소비교하기도 가능함.

#3번 : 함수로 바꾸기

def Maxvalue():
    list = []
    while True :
        insert = int(input("(입력을 멈추고 싶으면 0을 누르세요) 입력값: "))
        if insert != 0 : 
            list.append(insert)
            print(list)
        else:
            print(list)
            break
        
    
    
    for i in list :
        maxvalue=0
        if i > maxvalue:
            maxvalue=i
    print(maxvalue)

Maxvalue()