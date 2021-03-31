class Vscode:

    def execute(self):
        print("Terminal")
        print("Compiler")


class Pycharm:
    
    def execute(self):
        print("Terminal")
        print("Compiler")
        print("Conventions")


class Laptop:

    def code(self,ide):
        ide.execute()


ide = Vscode()
Laptop().code(ide)


ide = Pycharm()
Laptop().code(ide)
