# ALL THE OPERATIONS PERFORMNED ON THE LIST


list = ['Python','Java','React','CPP']

#Updating an element from the list
list[2] = 'R'  

print(list)  # ['Python', 'Java', 'R', 'CPP']


list.append("C")
print(list)  # ['Python', 'Java', 'CPP', 'C']

list.insert(3,"Cobol")
print(list)  # ['Python', 'Java', 'CPP', 'Cobol', 'C']

#New list Frameworks
list2=["Django","Spring","Larvel","Express"]

list.extend(list2)

print(list)        #['Python', 'Java', 'CPP', 'Cobol', 'C', 'Django', 'Spring', 'Larvel', 'Express']


# DELETING FROM THE LIST

del list[2]
print(list)       # ['Python', 'Java', 'Cobol', 'CPP', 'C', 'Django', 'Spring', 'Larvel', 'Express']


list.pop()
print(list)          # ['Python', 'Java', 'Cobol', 'CPP', 'C', 'Django', 'Spring', 'Larvel']

list.remove("C")
print(list)          # ['Python', 'Java', 'Cobol', 'CPP', 'Django', 'Spring', 'Larvel']

# REVERSING THE LIST

list.reverse()
print(list)          # ['Larvel', 'Spring', 'Django', 'CPP', 'Cobol', 'Java', 'Python']

list.sort()
print(list)          # ['CPP', 'Cobol', 'Django', 'Java', 'Larvel', 'Python', 'Spring']


# SLICING THE LIST
print("SLICING THE LIST")
print(list[:])        #['CPP', 'Cobol', 'Django', 'Java', 'Larvel', 'Python', 'Spring']
print(list[:6])       #['CPP', 'Cobol', 'Django', 'Java', 'Larvel', 'Python']
print(list[-3:-1])      #['Larvel', 'Python']
print(list[:-3])        #['CPP', 'Cobol', 'Django', 'Java']

