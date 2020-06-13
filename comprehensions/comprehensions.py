nums = [1,2,3,4,5,6,7,8,9,9,0,1,2,3]

my_list = [ n for n in nums ]
print(my_list)
print()

my_list = [ n*n for n in nums ]
print(my_list)
print()


my_list = [ n for n in nums if n%2 is 0]
print(my_list)
print()

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)
print()

names = ['Bruce','Clark','Peter','Logan','Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine','Deadpool']

#dictionary comprehension
my_dict = {name: hero for name, hero in zip(names,heros)}
print(my_dict)
print()

#set comprehension
my_set = {n for n in nums}
print(my_set)



# <-----------------output------------------------>

# $ python3 comprehensions.py
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 0, 1, 2, 3]

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 81, 0, 1, 4, 9]

# [2, 4, 6, 8, 0, 2]

# [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('d', 0), ('d', 1), ('d', 2), ('d', 3)]

# {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}

# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}