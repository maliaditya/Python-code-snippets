class Cars:
    def __init__(self,name):
        self.name = name

    def favouriteSportsCar(self):
        print("My faourite car is: " + self.name)


c = Cars("Ford Mustang Shelby GT350")
c.favouriteSportsCar()