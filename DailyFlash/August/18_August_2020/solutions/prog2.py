import array as arr
gen = range(1,10,2)

squares = [a*a for a in list(gen)]

array = arr.array('i',(squares))

print(array)