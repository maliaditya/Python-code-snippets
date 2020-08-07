'''
1  3  6  10
  12 15  19
     22 26
        30
        

1     1+2     3+3     6+4
        10+2    12+3   15+4
                19+3   22+4
                       26+30 '''
sum = 0
z =0
for i in range(1,5):
    print()
    for a in range(1,5):
        
        if a < i:
            print("  " , end=" ")
        else:
            sum+=a
            print(str(sum).zfill(2), end =" ")
            
        
