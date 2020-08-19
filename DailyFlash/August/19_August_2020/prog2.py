t=set()
name = input("Enter your name: ")
surname = input("Enter your surname: ")
# name ='Aditya'
# surname = "Mali"


for a in name:
   t.add(a)

for a in surname:
    t.add(a)

for a in t:
    print(a,end=" ")
