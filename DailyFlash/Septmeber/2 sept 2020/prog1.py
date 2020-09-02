

def factorial(num):
    if num == 1:
        return num
    return num * factorial(num-1)

def special_number(num,sum):
    if num == sum:
        print("pronic number")
    else: print("not a pronic number")

n=148
sum =0
for a in str(n):
    sum += factorial(int(a))


special_number(n,sum)

