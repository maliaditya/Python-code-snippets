space = 0
disp =4
for a in range(1,10):
    if a < 6:
        for b in range(1,6):
            if b >disp: 
                print("*",end = " ")
            else:
                print(" ",end = " ")

    else:
        for b in range(5): 
            if b > space:

                print("*",end = " ")
            else:
                print(" ",end = " ")
        space +=1
    disp -=1
    
    print()