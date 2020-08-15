def outer(start):
    state = start
    def inner(label):

        print(label,state)
        state += 1
        print(label,state)
    return inner

f= outer(0)
f('after inc')