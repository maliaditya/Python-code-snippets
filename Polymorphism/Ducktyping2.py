class Duck:

    def quack(self):
        print("Quack Quack")
    
    def Swim(self):
        print("Swiming")


class Person:
    
    def quack(self):
        print("Hey i am Quacking")
    
    def Swim(self):
        print("i can Swim")


obj = Duck()
obj2 = Person()

try:
    obj2.quack()
    obj2.Swim()
    print("It is a Duck")
except:
    print("not a duck")
