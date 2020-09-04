list1 = [ x*x for x in range(1,11) if x%2==0]+[ x*x*x for x in range(1,11) if x%2!=0]
list1.sort() 
print(list1)