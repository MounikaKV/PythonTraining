def sum(a,b):
    return a/b

def smart_sum(new_f):
    def inner(p,q):
        if p<q:
            p,q = q,p
        return new_f(p,q)
    return inner

s = smart_sum(sum)
print(s(2,4))