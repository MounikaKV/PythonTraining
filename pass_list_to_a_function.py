lst = ["mkv","mounika","laharimounika"]

def count_name_len(lst):
    leng=[]
    for i in lst:
        leng.append(len(i))
    return leng

lengs = count_name_len(lst)
print("First = {}, second = {}, third = {}".format(lengs[0], lengs[1], lengs[2]))