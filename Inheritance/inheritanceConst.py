class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Dog(Animal):
    
    def __init__(self,sound,name,color):
        super().__init__(name,color)
        self.sound = sound

    def animal(self):
        print("DOG")
        print("Name: ",self.name)
        print("color: ",self.color)
        print("sound:", self.sound)



obj = Dog("Woof woof","Tuffy","Black")
obj.animal()