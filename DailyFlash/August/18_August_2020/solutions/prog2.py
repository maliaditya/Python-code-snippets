import array as arr
gen_exp = (a**2 for a in range(10) if a %2 != 0)
print(type(gen_exp))

array = arr.array('i',(gen_exp))

print(array)
