class BritainKing:
    
    
    name = "Charles"

    def __init__(self):
        self.name = "Charles"


    def runmystatic(func):
        def inner(self=None):
            func()
        return inner


    @staticmethod
    def KingName():
        print(BritainKing.name)

    @runmystatic
    def Palace():
        print("Buckhingum")

    
    

obj = BritainKing()
obj.Palace()
obj.KingName()

