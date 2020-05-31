class Colony:
    Member = True
    
    @classmethod
    def Gym(cls):
        if cls.Member ==  True:
            print("Free")
        
    @staticmethod
    def my_house():
        print(Colony.Member)

    
Colony.Gym()
Colony.my_house()