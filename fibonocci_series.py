def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
n = int(input("Enter fibonacci series until : "))
fib(n)




######### First solution #######
'''
until = int(input("Enter until how many numbers you want to print : "))
def fib(until):
    list = [0, 1]
    first = 0
    second = 1
    for i in range(until):
        value = first+second
        first = second
        second = value
        list.append(value)
    print(list)

fib(until)
'''