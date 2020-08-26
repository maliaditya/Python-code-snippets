name = ' C o r e 2 w e b  )'

for a in range(3):
    if a%2==0:
        for b in range(18):
            if b%2==0:
                print("/",end="")
            else:
                print("\\",end="")
        print()
    else:
        for b in range(18):
            if b%2==0:
              print("|",end="")
            else:
                 print(name[b],end="")
        print()
      