class Addition:

    def addnum(self,a1=None, a2=None, a3=None):
        if a3==None and a2 == None:
            return a1
        elif a3 == None:
            return a1 + a2
        else:
            return a1+a2+a3


print(Addition().addnum(12,12))