disp = 4
p =1
for a in range(5):
    for b in range(5):
        if b < disp:
            print("",end=" ")
        else:
            if b == 4:
                print(p,end=" ")
                p +=1
            elif a > 3:
                print(b+1,end = " ") 
            elif b == disp:
                print(1,end=" ")
            else:
                print(" ",end = " ")
    
    disp -=1
    print()