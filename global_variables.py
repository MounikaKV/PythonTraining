a=10
b=20
c=30

def something():
    #global a only then the outside a will change to what we change inside
    a = 15
    x=globals()["a"]
    print("a inside ",a)
    globals()['a'] = 15 # This chnages the gloabal value
something()
print("a outside ",a)
