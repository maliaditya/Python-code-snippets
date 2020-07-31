
# lastnum = 1 
# for a in range(1,6):
# 	print()

# 	for b in range(lastnum,a+lastnum):
# 		print(b,end=" ")
		
# 	lastnum = b
import time
for a in range(6):
	print()
	for b in range(5):
		time.sleep(0.1)
		print("*", end=" ")

for a in range(6):
	print()
	for b in range(5):
		time.sleep(0.1)
		if a > 0 and a<5:
			if b > 0 and b<4:
				print(" " , end=" ")
			else:
				print("*",end=" ")
		else:
			print("*", end=" ")
		
for a in range(6):
	print()
	for b in range(5):
		time.sleep(0.1)
		print("*", end=" ")
		
