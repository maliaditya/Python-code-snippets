import copy as cp
# Shallow copy
list1 = ["Java","Python","C","CPP","JavaScript",]
print(list1)
list2 = cp.copy(list1)
list2.append("Go")
print(list2)

list1 = ["Java","Python","C","CPP","JavaScript",["Django","Flask","Spring boot"]]
print(list1)
list2 = cp.copy(list1)
list2[5].append("Go")
print("After Changes")

print(list2)
print(list1)

#Deep Copy
print("")
print("")
print("Deep Copy")
list1 = ["Java","Python","C","CPP","JavaScript",["Django","Flask","Spring boot"]]
print(list1)
list2 = cp.deepcopy(list1)
list2[5].append("Go")
print("After Changes")

print(list2)
print(list1)



# Dictionary Copy method

print("COPY DICT")


dict = {"C":1977 , "Java": 1995, "Python":1992, "CPP":1979, "Frameworks" :{"Django":2006 , "Flask":2011}}

years = cp.copy(dict)

print(dict)
years["Frameworks"]["Flask"] = 2010
print("After Changes")
print(years)
print(dict)


print()
print()
print("DEEPCOPY DICT")
dict = {"C":1977 , "Java": 1995, "Python":1992, "CPP":1979, "Frameworks" :{"Django":2006 , "Flask":2011}}

years = cp.deepcopy(dict)

print(dict)
years["Frameworks"]["Flask"] = 2010
print("After Changes")
print(years)
print(dict)

print()
print()
print("Count Method ")
shares = [("Google","Jio"),("Jio","Facebook"),("Netflix","Amazon"),"Microsoft"]
x = shares.count(("Google","Jio"))
print(x)

print("Tuple")
shares = (("Google","Jio"),("Jio","Facebook"),("Netflix","Amazon"),"Microsoft")
x = shares.count(("Google","Jio"))
print(x)

print()
print()
print("All Method")
print("Tells wether there is no 0 element if true")

dict = {"C":1977 , "Java": 1995, "Python":1992, "CPP":1979, "Frameworks" :{"Django":2006 , "Flask":2011}}
x =all(dict)
print(x)


print()
print()

print("any()")
print("Tells wether there is no 0 element if true")

dict = {"C":1977 , "Java": 1995, "Python":1992, "CPP":1979, "Frameworks" :{"Django":2006 , "Flask":2011}}
x =all(dict)
print(x)

print()
print()

print("len()")
IndianBuss =["Ambani","Tata","Adani","Birla"]
print(len(IndianBuss))


