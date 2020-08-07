inp = 'n' + input("enter a palindrome: ")

flag =0
for a in range(1,len(inp)-1//2):
    if inp[a] == inp[-a]:
        flag +=1
    else:
        print("not palindrome")


if flag == len(inp)//2:
    print(" palindrome")


