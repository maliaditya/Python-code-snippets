auction = {'Watson' : 'CSK','Raina':'CSK','Dhoni':'CSK','Rohit':'MI','Malinga':'MI','Pandya':'MI'}

CSK = [a for a in auction if auction[a] == 'CSK']

MI = [a for a in auction if auction[a] == 'MI']

print(CSK)
print(MI)
