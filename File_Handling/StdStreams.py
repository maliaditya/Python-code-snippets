import sys
print("enter enter any message")
mess = sys.stdin.readline()
print("Your message is:")
sys.stdout.write(mess)
sys.stderr.write("error Message")