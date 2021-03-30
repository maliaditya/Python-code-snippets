n=10
prime = False
for a in range(2,n):
    if n%a == 0:
        prime = True

if prime == False:
    print("number is a prime number")
else:
    print("not a prime number")
