
def isPrime(n):
    count = 0
    for i in range(2,int(n/2)):
        if n%i ==0:
            count+=1
            return False
    
    if count == 0:
        return True

def reverse(s): 
    str = "" 
    for i in s: 
        str = i + str
    return str

n = 23
p = isPrime(n)

if p == True:
    r = reverse(str(n))


p = isPrime(int(r))
if p == True:
    print("is a Emirp number")
else:
    print("is not a Emirp number")
