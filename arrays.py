from array import *

arr = array("i",[])
num = int(input("Enter array size : "))
for i in range(num):
    x = int(input("Enter an element : "))
    arr.append(x)

print(arr)

indx = 0
y = int(input("Enter element to search : "))
for j in arr:
    if y == j:
        print("Found at index",indx)
        break
    indx+=1
else:
    print("Not found")