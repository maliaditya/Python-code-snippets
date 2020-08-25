gloves = [35,30,25,40,50,20]
masks = [50,60,30,70,40,90]



for a in gloves:
    for b in masks:
        if a +b <=90:
            print(a+b , end=" ")
    print()