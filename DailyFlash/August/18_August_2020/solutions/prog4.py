auction = {'Watson' : 'CSK','Raina':'CSK','Dhoni':'CSK','Rohit':'MI','Malinga':'MI','Pandya':'MI'}

CSK = []

MI = []

for a in auction:
    if auction[a] == 'CSK':
        CSK.append(a)
    else:
        MI.append(a)

print(CSK)
print(MI)