import sys

code_part = "print('Hello World')"

orig_stdout = sys.stdout
sys.stdout = open('file.txt', 'w')
exec(code_part)
sys.stdout.close()
sys.stdout=orig_stdout
output = open('file.txt', 'r').read()

print(output)