ary = [ [], [], [], [], [] ]

cnt=0
for ary2 in ary:
    for j in range(5): 
        cnt = cnt + 1
        ary2.append(cnt)
        print(ary2)

print(ary)