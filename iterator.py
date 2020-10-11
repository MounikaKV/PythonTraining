# x = [1,2,3,4]
# it = iter(x)
# print(it.__next__())
# print(next(it))
# print(it.__next__())
# print(next(it))
class Topten:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

x = Topten()

print("Obj : ",x)

print("Values : ", x.__next__());
print("Values : ", x.__next__());
print("Values : ", x.__next__());
print("Values : ", x.__next__());
print("Values : ", x.__next__());
print("Values : ", x.__next__());
print("Values : ", x.__next__());
print("Values : ", x.__next__());
print("Values : ", x.__next__());
print("Values : ", x.__next__());
