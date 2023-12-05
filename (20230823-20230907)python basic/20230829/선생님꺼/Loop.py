# while
# for(int i=1; i<10; i++)  자바코드
i=0
while i<10:
    i=i+1
    print("%2dX%2d=%2d" % (2, i, 2*i))

i=0
while True:
    i=i+1
    if i>=10:
        break
    print("%2dX%2d=%2d" % (2, i, 2*i))

