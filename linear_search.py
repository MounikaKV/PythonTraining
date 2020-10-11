# Using For loop
x = [1,2,3,4,5,6]
y = 3

def Search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            return i
    return false
pos = Search(x,y)

if Search(x,y):
    print("Found the element at position ", pos)
else:
    print("Not found")

# Using while loop
# x = [1,2,3,4,5,6]
# y = 6
#
# def Search(list, n):
#     i = 0
#     while i<len(list):
#         if list[i] == n:
#             return i
#         i+=1
#     return False
#
# pos = Search(x,y)
# if Search(x,y):
#     print("Found the element at position ", pos)
# else:
#     print("Not found")