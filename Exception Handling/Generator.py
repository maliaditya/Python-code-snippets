
def my_generator():
    try:
        for i in range(5):
            print ('Yielding', i)
            yield i
    except GeneratorExit:
        print ('GeneratorExit caught')
  
g = my_generator()
print (g.__next__())
g.close()