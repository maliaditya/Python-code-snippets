name = '   C o r e 2 w e b  '

for a in range(3):
    if a==0:
        for b in range(18):
            if b%2==0:
                print("/",end="")
            else:
                print("\\",end="")
        print()
    elif a==1:
        print("(",end="")
        for b in range(3,18):
            
            if b%2==0:
              print("|",end="")
            else:
                 print(name[b],end="")
        print(")")
    else:
        for b in range(6):
            print("\\_/",end="")
          
        print()
      