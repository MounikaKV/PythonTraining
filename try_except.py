a = 5
b = 0
try:
    k = 5a
    if a == k:
        print("A == K")
    elif b == k:
        print("B == K")
    else:
        print("K is not the same as either A or B")

except ValueError as e:
    print("Value Error : ", e)

except NameError as e:
    print("NameError : ",e)

except Exception as e:
    print("Something went wrong!",e)

finally:
    print("Successfully executed :\)")
