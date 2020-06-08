tuple = "Python", "C", "C++", "Java"
print(type(tuple))  #<class 'tuple'>

tuple1 = ()
print(type(tuple1))  #<class 'tuple'>


tuple2 = ("Python")
print(type(tuple2))# <class 'str'>

# Commas are required in tuple though paranthesis are optional you should give the for packing amibiguity

tuple3 = ("Python",)
print(type(tuple3))  #<class 'tuple'>


print("SLICING in Tuple")
tuple4 = ('Python', 'Java', 'Cobol', 'CPP', 'C', 'Django', 'Spring', 'Larvel', 'Express')
print(tuple4[:])        
print(tuple4[:6])       
print(tuple4[-3:-1])      
print(tuple4[:-3])        
