
num = list(int(x) for x in input("Enter List of Numbers: ").split())



def largestNo():
    lagestNumber = num[0]
    for a in num:
        if lagestNumber < a:
            lagestNumber = a
    return lagestNumber



def LCM():
    largestNum = largestNo()
    temp = largestNum
    i = 2
    for a in num:

        while True:
            if largestNum % a == 0:
                break
            else:

                largestNum = temp
                largestNum *= i
                i += 1
                

    return largestNum


print(LCM())



