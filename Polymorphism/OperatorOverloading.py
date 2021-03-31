class  student:

    def __init__(self,m1):
        self.m1 = m1
        
    
    def __add__(o1,o2):
        return o1.m1 + o2.m1


obj1 = student(12)
obj2 = student(8)


print( obj1 + obj2 )