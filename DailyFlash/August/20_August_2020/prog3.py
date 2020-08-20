dc = {'Germany':'Berlin','Italy':'Venice','France':'Versailes','Cannada':'Quebec City'}
c = 0
for x,y in dc.items():
    if c%2==0:
        print(x)
    else:
        print(y)
    c +=1