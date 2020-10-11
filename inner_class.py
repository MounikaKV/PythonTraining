class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)

    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 16

s1 = Student("Mkv",26)
s1.show()
print(s1.lap.brand)
