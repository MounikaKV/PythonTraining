class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def __config__(self):
        print("Config is :", self.cpu, self.ram)

    def update(self):
        self.cpu = "NO idea"

    def compare(self,other):
        return self.cpu == other.cpu

comp1 = Computer("i5",16)
comp2 = Computer("i7", 32)

comp1.cpu = "Mkv"

comp1.__config__()
comp2.__config__()

print(comp1.compare(comp2))

comp1.cpu = "i7"

print(comp1.compare(comp2))
