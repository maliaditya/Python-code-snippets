#lucas number

lucas_number = [2,1]

for a in range(7):
    for  b in range(2):
        if a == len(lucas_number):
            lucas_number.append(lucas_number[a-2]+lucas_number[a-1])


print(lucas_number)