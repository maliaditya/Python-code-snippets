prime_list = []
last=100
for num in range(last):
	flag = 0
	for a in range(2,int(num/2)):
		if num%a ==0:
			flag = 1

	if flag == 0:
		prime_list.append(num)
	else:
		continue

print(prime_list)