names = ['aditya','aadesh','nayan']

f = 0
b =-1

for a in names:
    c = list(ord(x) for x in a)
    b = list(ord(x) for x in a)
    b.reverse()

    for x in range(len(c)):
        if c[x] == b[x]:
            if x == len(c)-1:
                print(a,"will get the discount")
            continue
        else:
            print("not valid")
            break
        f+=1
        b -= -1
