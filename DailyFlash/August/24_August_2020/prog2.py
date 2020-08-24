def strcmp(str1,str2):
    diff = 0
    for a in range(len(str1)):
        diff = ord(str1[a]) - ord(str2[a])
        if diff != 0:
            print(diff)
            break

        
    if diff == 0:
        print(diff)
    

        
            



strcmp(input("Enter the 1st String: "),input("Enter the 2nd String: "))
