class Squares:
    def __init__(self,start,stop):
        self.value = start -1
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


for i in Squares(1,5):
    print(i, end = " " )

# x = Squares(1,5)
# I = iter(x)
# next(I)
# next(I) 
# next(I)