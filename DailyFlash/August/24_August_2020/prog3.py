def strcmp(str1,str2):
    str1 = [x.lower() for x in str1]
    str2 = [x.lower() for x in str2]
    isAnagram = True
    for a in range(len(str1)):
       if str1[a] not in str2:
            print("Not an Anagram!")
            isAnagram = False

    if isAnagram is True:
        print("Is an Anagram!")

        
strcmp(input("Enter the 1st String: "),input("Enter the 2nd String: "))
