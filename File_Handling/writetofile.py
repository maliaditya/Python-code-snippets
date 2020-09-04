import sys
code = 'print(int(input())+int(input()))'

input_part = [1,2]
def input():
            a = input_part[0]
            del input_part[0]
            return a

a = sys.stdout

sys.stdout = open('file.txt','w')
exec(code)
sys.stdout.close()

sys.stdout = a

output = open('file.txt','r').read()
print("op ",output)

