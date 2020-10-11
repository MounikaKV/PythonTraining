class PyCharm:
    def execute(self):
        print("Compiling and Running..")

class MyEditor:
    def execute(self):
        print("Running my own editor")

class Laptop:
    def code(self, ide):
        ide.execute()

ide = PyCharm()
l = Laptop()
l.code(ide)
ide = MyEditor()
l.code(ide)