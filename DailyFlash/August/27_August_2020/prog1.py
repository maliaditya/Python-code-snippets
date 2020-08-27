n = input("Enter a number: ")
num = [int(x) for x in n]
l = len(num)
sum =0

for a in num:
    sum += a**l


if sum == int(n) :
    print( sum , "Is an narccistic Number")

else:
    print("Not a narccistic number")

