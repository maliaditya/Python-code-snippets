spaces = 5
bspace = 5
disp = 0
for a in range(5):
    for b in range(1,10):
        if b < spaces or b > bspace:
            print(" ",end = " ")
        else:
            if b > 5:
                disp -= 1
                print(disp,end=" ")
                
            else:
                disp+=1
                print(disp,end=" ")
                
                

    spaces-=1
    bspace+=1
    print()