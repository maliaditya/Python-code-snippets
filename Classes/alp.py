space = 4
bspace =4
mspace = 3
for a in range(5):
    print()
    for b in range(9):
        if(b<space):
            print(" ", end=" ")
        else:
            if(b>bspace):
                print(" ", end=" ")
            else:
                if b==space or b==bspace:
                    print(a,end=" ")
                else:
                    print(" ", end=" ")

    space -= 1 
    bspace += 1 
    