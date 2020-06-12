prog_Lang = {1:"Python", 2:"Java-script", 3:"C",
            4:"C++", 5:"Java"}

# Retive single value
print(prog_Lang[1])

print(prog_Lang.get(3,4))


# Updating the dictionary


prog_Lang[1] = 'Go'

print(prog_Lang[1])


prog_Lang.update({1:"Java-script",2:"Python"})
print(prog_Lang)


print(prog_Lang.keys())
print(prog_Lang.values())
print(prog_Lang.items())



print()
print('looping throug keys')
for x in prog_Lang:
    print(x)



print()
print('looping through Values')
for x in prog_Lang.values():
    print(x)


print()
print('looping through Keys & Values')
for x,y in prog_Lang.items():
    print(x,y) 

del(prog_Lang[1])

# Output
# C
# Go
# {1: 'Java-script', 2: 'Python', 3: 'C', 4: 'C++', 5: 'Java'}
# dict_keys([1, 2, 3, 4, 5])
# dict_values(['Java-script', 'Python', 'C', 'C++', 'Java'])
# dict_items([(1, 'Java-script'), (2, 'Python'), (3, 'C'), (4, 'C++'), (5, 'Java')])

# looping throug keys
# 1
# 2
# 3
# 4
# 5

# looping through Values
# Java-script
# Python
# C
# C++
# Java

# looping through Keys & Values
# 1 Java-script
# 2 Python
# 3 C
# 4 C++
# 5 Java