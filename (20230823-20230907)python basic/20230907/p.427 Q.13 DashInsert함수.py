def DashInsert(a):
    answer = ''
    for i in range(len(a)):
        if i < (len(a))-1 :
            if int(a[i]) % 2 == 0 and int(a[(i+1)]) % 2 == 0 :
                answer = answer + a[i] + '*'
            elif int(a[i]) % 2 == 1 and int(a[(i+1)]) % 2 == 1 :
                answer = answer + a[i] + '-'
            else:
                answer = answer + a[i]                    
        i = i + 1
    answer = answer + a[(len(a)-1)]
    return answer

a='1224'
print(DashInsert(a))