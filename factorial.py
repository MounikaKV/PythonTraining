def fact(n):
    ans = 1
    if n<0:
        ans = print("Invalid input : Factorial exists only for positive numbers!")
    elif n<=1:
        ans = 1
    else:
        for i in range(1, n+1):
            ans*=i
    return ans

n = int(input("Enter value for n : "))
factorial = fact(n)
print("Factorial of {} : {}".format(n, factorial))
'''
def factorial(n):
    
    if n<0:
        y = print("Invalid input, n cannot be negative!")
    elif n<=1:
        y = 1
    else:
        for i in range(1,n):
            y=i
    return y
value = 5
ans = 1
for i in range(1,value+1):
    x = factorial(i)
    print(i, x, ans)
    ans = ans*x
'''