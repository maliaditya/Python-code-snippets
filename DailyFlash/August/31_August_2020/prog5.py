p = 1
space = 0
disp =4
d = 2
for a in range(1,10):
    if a < 6:
        for b in range(1,6):
            if b >disp: 
                print(p,end = " ")
                p += 1

            else:
                print("",end = " ")

    else:
        for b in range(5): 
            if b > space:
                print(p,end = " ")
                p +=1    
            else:
                print("",end = " ")
        d+=1
        space +=1

    disp -=1
    if a <5: p = 1
    else: p = d 
    print()