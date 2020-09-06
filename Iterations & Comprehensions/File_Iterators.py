# f = open('even &odd.py')
# f.readline()
# f.readline()
#  #the __next__ i s identical and better way to iterate the file

#  f.__next__() or next(f) are both similar

#iterationg file using for loop
for a in open('test.txt'):
    print(a)


list = [12,2,3,4,5,4]

a = iter(list)
next(a)