import sys
a = sys.stdout
sys.stdout = open('file.txt','w')
print("hello world")
sys.stdout.close()
sys.stdout = a

output = open('file.txt','r').read()
print(output)

