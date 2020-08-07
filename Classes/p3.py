
r = 0
temp = 0
for a in range(100,500):
    while(a!=0):
        temp = a %2
        r += temp*temp*temp
        a = a/10

    if temp == a:
        print(temp)

    temp =0
    r=0



