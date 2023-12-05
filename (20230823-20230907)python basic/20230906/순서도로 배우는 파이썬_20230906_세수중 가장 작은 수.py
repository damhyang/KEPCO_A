a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

# 방법1. 
list = [a,b,c]
mini = list[0]
for i in range(1, len(list)):
    if mini > list[i]:
        mini = list[i]
print(mini)


# 방법2. 
# a>b>c
# a>c>b
# b>a>c
# b>c>a
# c>a>b
# c>b>a

# 방법3 : 최소수만 구하면 된다. 
if a<b:
    if a<c:
        print(a)
    else:
        print(c)
else:    
    if b<c:
        print(b)
    else:
        print(c)
        
# 방법4 : min()함수를 사용한다. 
list = [a,b,c]
m = min(list)
print(m)