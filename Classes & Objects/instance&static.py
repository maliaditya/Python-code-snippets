class class_room:
    teacher = "Shashi"
    def __init__(self,student):
        self.student = student

    
obj1 = class_room("Aditya")
obj2 = class_room("Aditya")
print("static",obj1.teacher)
print("static",obj2.teacher)
class_room.teacher = "Khan sir"

print(obj1.student)
print(obj2.student)
print(id(obj2))
print(id(obj1))
print("static",obj1.teacher)
print("static",obj2.teacher)

