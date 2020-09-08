import numpy
import inspect
a = inspect.getfile(numpy).split('/')
for x in a:
    print(x)
