n=int(input("enter width: " ))
 
for i in range(0,n): 
 
    for j in range(0,i+1): 
        print("*",end=" ") 
         
    for k in range(n-1,i,-1): 
        print("  ",end="  ") 
         
    for j in range(0,i+1): 
        print("*",end=" ") 
         
    print("\n",end='') 
     
   
    	 
for i in range (n,0,-1):  
     
    for j in range(i,0,-1): 
         print("*",end=" ") 
          
    for k in range(0,n-i): 
        print("  ",end="  ") 
         
    for j in range(1,i+1): 
        print("*",end=" ") 
     
    print("\n",end='')