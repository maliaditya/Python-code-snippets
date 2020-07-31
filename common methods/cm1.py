print()
print("     min() & max()   ")
print()

list =  [10,28,22,67.2,45]
set = {"C","Java","Python","CPP"}
dict = {100000 : "Iphone",80000:"Samsung",70000:"Oneplus"}
print(">>>" ,min(list,default=8))
print(">>>" , min(set,key=len))
print(">>>" , min(dict))
print("max")
print(">>>" ,max(list,default=8))
print(">>>" , max(set,key=len))
print(">>>" , max(dict))

print()
print()

list1 = [10,20,30,40,50]
list2 = [60,70,80,90]
list3 = [list1,list2]
print(">>>" ,min(list3))
list4 =  [10,28,22,67.2,45]
list5 = ["C","Java","Python","CPP"]
list3 = [list5,list4]
print(list3)


print()
print()


print("     Sorted()    ")
print()

list5 = ["C","Java","Python","CPP"]
list5 = {"C","Java","Python","CPP"}
print(sorted(list5))
print(sorted(list5,reverse = True))
print(sorted(list5,key = len))
print(sorted(list5,key = len,reverse = True))
print(sorted(list5,reverse = True,key = len))



for a in sorted(dict):

    print(a,dict[a])


friends = ['Aadesh',"Drumil","Shubham","Kundan","Varun" ]
Colleges = ["Zeal","Symboisys","DY","Matoshree","Nahi mahit"]
print(zip(friends,Colleges))

 x = list(zip(friends,Colleges))
 x
[('Aadesh', 'Zeal'), ('Drumil', 'Symboisys'), ('Shubham', 'DY'), ('Kundan', 'Matoshree'), ('Varun', 'Nahi mahit')]
 x,y = zip(*x)
