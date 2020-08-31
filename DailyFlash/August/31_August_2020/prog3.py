
for a in range(1,10):
    if a < 6:
        for b in range(6):
            if b <a: 
                print("*",end = " ")
    else:
        for b in range(6,11):
            if b >a: 
                print("*",end = " ")
            
    print()