import sys
num = int(sys.argv[1])
#num = int(input("Enter the number to check : "))
for i in range(2,num):
    if (num % i == 0):
        print("Not prime")
        break
else:
    print("Prime")

